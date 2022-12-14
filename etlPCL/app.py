

# Below code came from Tangan Zhao's code base
# I tweaked them  to run in my local PC 
# 5-1-2022


import importlib
import os
import time
import configparser
import concurrent.futures
import subprocess
from datetime import date
import uuid

from csv import reader
from csv import DictReader
import util.dbTool  as dbTool

from bo.mysql.variant_drug   import variant_drug   as drugBO
from da.mysql.variant_drugDA import variant_drugDA as drugDA
from bo.mysql.boList         import boList

""" Convert mm/dd/yyyy to yyyy/mm/dd  """
def toYYYYMMDD(dateStr):
    fullYears = ['/2019','/2020','/2021','/2022','/2023','/2024','/2025','/2026','/2027','/2028','/2029','/2030']

    simpleYears = ['/19','/20','/21','/22','/23','/24','/25','/26','/27','/28','/29','/30']

    tempStr=''

    for fy in fullYears: 
        if dateStr.endswith(fy):
            tempStr =fy.replace('/','')+'/'+ dateStr[0:(len(dateStr)-5)]
    if len(tempStr.strip())==0:
        for sy in simpleYears: 
            if dateStr.endswith(sy):
                tempStr =sy.replace('/','20')+'/'+ dateStr[0:(len(dateStr)-3)]
    if len(tempStr.strip())==0:
        print('Please  chck formate for this date string %s '%dateStr)
 
    #print('Before comvert %s, after conversion %s'%(dateStr,returnStr))
    return tempStr

""" Convert date string to date object """
def to_Date_wrong(dateStr):
    simpleYears = ['/19','/20','/21','/22','/23','/24','/25','/26','/27','/28','/29','/30']

    for sy in simpleYears: 
        if dateStr.endswith(sy):
            dateStr = dateStr[0:(len(dateStr)-3)]+ (sy.replace('/','/20'))


    dateObj = None
    formats = ['%m/%d/%Y','%m/%d/%y']
    for fmt in formats:
        if dateObj is not None:
            return dateObj

        try:
            dateObj = datetime.strptime(dateStr, fmt)
        except:
            pass



def main():
    file1='Drug_database_master_20220930.txt'
    file2='In_Vivo_Database_Master_20220916.txt'
    file3='Linked_report_database_20220715.txt'
    file4='ODP_database_master_20220930.txt'
    file5='OOS_database_master_20220930.txt'
    file6='Variant_database_master_20220930.txt'
    file7='related_resources-20220617.txt'

    myDir     = os.path.dirname(os.path.realpath(__file__))  

    start_time=time.time()

    #Task 1:  
    dataFileName=file1

    dataFileFullPath  = '%s/%s/%s' % (os.path.abspath('.'),'etlData',dataFileName) ##<--dataset in curret path's sub folder 'etlData'
    os.system('vim +"set nobomb | set fenc=utf8 | x" '+dataFileFullPath)
    insertVal=None
    with open(dataFileFullPath, 'r') as f:
         
        myCSVReader = reader(f,delimiter='\t', quotechar='"')
         
        insertVal = list(map(tuple, myCSVReader))

    insertSQL="INSERT INTO variant_drug (id,drug_name,drug_class,priority,alias1,alias2,alias3,alias4,alias5,unii,cas,drug_company) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    insertVal=insertVal[1:]  #remove the header from myCSVReader

    drugDA.runSQL('SET SQL_SAFE_UPDATES = 0')

    drugDA.runSQL('commit')
    drugDA.runSQL('truncate table variant_drug;') #<---delete all recodrs in table variant_drug
  
    
    drugDA.runSQL('commit')
    drugDA.runInsertListOfTuple(insertSQL, insertVal)
    drugDA.runSQL('commit')
   
    drugDA.runSQL('update variant_drug set date_updated=now();')
     
    drugDA.runSQL('commit')
    drugDA.runSQL('SET SQL_SAFE_UPDATES = 1')
    drugDA.runSQL('commit')
    print('\n---total records were inserted into table variant_drug is: '+str(len(insertVal))+' from file '+dataFileFullPath)

    #Task 2:  
    dataFileName=file2

    dataFileFullPath  = '%s/%s/%s' % (os.path.abspath('.'),'etlData',dataFileName) ##<--dataset in curret path's sub folder 'etlData'

   
    os.system('vim +"set nobomb | set fenc=utf8 | x" '+dataFileFullPath)

 
    insertVal=[]
    listOfDicts = []
    with open(dataFileFullPath,'r') as f:  

        listOfDicts = [
            {k: v for k, v in row.items()}  
            for row in DictReader(f, skipinitialspace=True, delimiter='\t')
        ]

    for dt in listOfDicts:    

            if dt['Report_Number']:

                 
                reportedDate = toYYYYMMDD(dt['Reported_Date'])
                dataUpdatedDate = toYYYYMMDD(dt['Data_Updated_Date'])
                 
                insertVal.append((
                    dt['Report_Number'],
                    dt['Provider'],
                    dt['Title'],

                    dt['Data_Source'],
                    reportedDate,
                    dataUpdatedDate,

                    dt['Study_Type'],
                    dt['Therapeutic_Classes'],
                    dt['Therapeutic_Agents'],

                    dt['Model'],
                    dt['Model_Strain'],

                    dt['Model_Source'],
                    dt['Therapeutic_1_Class'],
                    dt['Therapeutic_1'],

                    dt['Administration_Method_1'],
                    dt['Dose_1'],
                    dt['Regimen_1'],

                    dt['Treatment_1_Notes'],
                    dt['Therapeutic_1_Details'],

                    dt['Therapeutic_2_Class'],
                    dt['Therapeutic_2'],
                    dt['Administration_Method_2'],
                    dt['Dose_2'],

                    dt['Regimen_2'],
                    dt['Treatment_2_Notes'],
                    dt['Therapeutic_2_Details'], 

                    dt['Variants'],
                    dt['Variant_Modifications'],
                    dt['WHO_Designation'],

                    dt['Reference_Strain'],
                    dt['Inoculation_Method'],
                    dt['Inoculation_Dose'],

                    dt['Challenge_Notes'],
                    dt['Challenge_Details'],
                    dt['Clinical_Manifestastions'],

                    dt['Viral_Load'],
                    dt['Histopathology'],
                    dt['Neutralization'],

                    dt['Antibody_Response'],
                    dt['Other_Database_Report_Number'],
                    dt['Animal_Models_Linked_Page'],
                    
                    dt['Transmission'],
                    dt['Rechallenge']
                ))


    insertSQL="""
            insert into variant_in_vivo (
                report_number, provider, title,
                data_source, reported_date, data_updated_date,
                study_type, therapeutic_classes, therapeutic_agents,
                model, model_strain, 
                model_source, therapeutic_1_class, therapeutic_1,
                administration_method_1, dose_1, regimen_1,
                treatment_1_notes, therapeutic_1_details,
                therapeutic_2_class, therapeutic_2, administration_method_2, dose_2, 
                regimen_2, treatment_2_notes, therapeutic_2_details,
                variants, variant_modifications, who_designation,
                reference_strain, inoculation_method, inoculation_dose,
                challenge_notes, challenge_details, clinical_manifestastions, 
                viral_load, histopathology, neutralization,
                antibody_response, other_database_report_number, animal_models_linked_page,
                transmission,rechallenge 
            ) 
            VALUES (
                %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s,
                %s, %s,
                %s, %s, %s,
                %s, %s, %s,
                %s, %s, 
                %s, %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s
               ,%s, %s
            )
           """
 
    mysql="truncate table variant_in_vivo" #<---delete all recodrs in table 
    drugDA.runSQL(mysql) 
    drugDA.runSQL('commit')
    drugDA.runInsertListOfTuple(insertSQL, insertVal)
    drugDA.runSQL('commit')

    drugDA.runSQL('SET SQL_SAFE_UPDATES = 0')
    drugDA.runSQL('update variant_in_vivo set data_uploaded_date=now()')
    drugDA.runSQL('SET SQL_SAFE_UPDATES = 1')
    drugDA.runSQL('commit')     

    print('\n---total records were inserted into table variant_in_vivo is: '+str(len(insertVal))+' from file '+dataFileFullPath)

    #Task 3:  
    dataFileName=file3

    dataFileFullPath  = '%s/%s/%s' % (os.path.abspath('.'),'etlData',dataFileName)  
    os.system('vim +"set nobomb | set fenc=utf8 | x" '+dataFileFullPath)
 
    insertVal=None
    with open(dataFileFullPath, 'r') as f:
         
        myCSVReader = reader(f,delimiter='\t', quotechar='"')
         
        insertVal = list(map(tuple, myCSVReader))
     
    insertSQL="insert into variant_linked_report (report_number,linked_report_number, linked_report_version) VALUES  (%s, %s, %s)"
    insertVal=insertVal[1:]   

    mysql="truncate table variant_linked_report"  
    drugDA.runSQL(mysql) 
    drugDA.runSQL('commit')
    drugDA.runInsertListOfTuple(insertSQL, insertVal)
    drugDA.runSQL('commit')

    drugDA.runSQL('SET SQL_SAFE_UPDATES = 0')
    drugDA.runSQL('update variant_linked_report set updated_date=now()')
    drugDA.runSQL('SET SQL_SAFE_UPDATES = 1')
    drugDA.runSQL('commit')     
    print('\n---total records were inserted into table variant_linked_report is: '+str(len(insertVal))+' from file '+dataFileFullPath)



    

    #Task 5:  
    dataFileName=file5

    dataFileFullPath  = '%s/%s/%s' % (os.path.abspath('.'),'etlData',dataFileName) ##<--dataset in curret path's sub folder 'etlData'

     
    os.system('vim +"set nobomb | set fenc=utf8 | x" '+dataFileFullPath)

   
    
    insertVal=[]
    listOfDicts = []
    with open(dataFileFullPath,'r') as f: #<---first import to List Of Dict

        listOfDicts = [
            {k: v for k, v in row.items()}  
            for row in DictReader(f, skipinitialspace=True, delimiter='\t')
        ]

    for dt in listOfDicts:   

            if dt['oos_report_number']:   

               
                oos_data_date = toYYYYMMDD(dt['oos_data_date'])
                 
                insertVal.append((
                    dt['oos_report_number'],
                    dt['oos_data_provider'],
                    dt['oos_data_title'],

                    dt['oos_data_source'],
                    dt['oos_data_source_2'],
                    oos_data_date,
                    dt['oos_data_type'],
                    dt['oos_assay_type'],

                    dt['oos_viral_lineage'],
                    dt['oos_drug_name']

                ))


    insertSQL="insert into variant_oos (report_number, data_provider, data_title,data_source, data_source_2, data_date,data_type, assay_type, viral_lineage, drug_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,  %s, %s)"
 

    mysql="truncate table  variant_oos" 
    drugDA.runSQL(mysql)
    drugDA.runSQL('commit') 
    drugDA.runInsertListOfTuple(insertSQL, insertVal)
    drugDA.runSQL('commit')

    drugDA.runSQL('SET SQL_SAFE_UPDATES = 0')
    drugDA.runSQL('update variant_oos set data_uploaded_date=now()')
    drugDA.runSQL('SET SQL_SAFE_UPDATES = 1')
    drugDA.runSQL('commit')     

    print('\n---total records were inserted into table variant_oos is: '+str(len(insertVal))+' from file '+dataFileFullPath)

    #Task 6  
    dataFileName=file6 

    dataFileFullPath  = '%s/%s/%s' % (os.path.abspath('.'),'etlData',dataFileName) ##<--dataset in curret path's sub folder 'etlData'

    
    os.system('vim +"set nobomb | set fenc=utf8 | x" '+dataFileFullPath)

    
    
    insertVal=None
    with open(dataFileFullPath, 'r') as f:
         
        myCSVReader = reader(f,delimiter='\t', quotechar='"')
         
        insertVal = list(map(tuple, myCSVReader))
    

    insertSQL="insert into viral_meta (id,viral_lineage,viral_classification,viral_rank, WHO_name) VALUES (%s, %s, %s, %s,%s)"
    insertVal=insertVal[1:]   

    mysql="truncate table viral_meta"  
    drugDA.runSQL(mysql) 
    drugDA.runInsertListOfTuple(insertSQL, insertVal)

    drugDA.runSQL('commit')     
    drugDA.runSQL('SET SQL_SAFE_UPDATES = 0')
    drugDA.runSQL('update viral_meta set date_updated=now()')
    drugDA.runSQL('SET SQL_SAFE_UPDATES = 1')
    drugDA.runSQL('commit')     
    print('\n---total records were inserted into table viral_meta is: '+str(len(insertVal))+' from file '+dataFileFullPath)



    #Task 4:  
    dataFileName=file4

    dataFileFullPath  = '%s/%s/%s' % (os.path.abspath('.'),'etlData',dataFileName) 

    
    os.system('vim +"set nobomb | set fenc=utf8 | x" '+dataFileFullPath)

     
    insertVal=[]

     
    listOfDicts = []
    with open(dataFileFullPath,'r') as f: #<---first import to List Of Dict

        listOfDicts = [
            {k: v for k, v in row.items()}  
            for row in DictReader(f, skipinitialspace=True, delimiter='\t')
        ]
     
    listOfDicts = list(filter(lambda d: len(d['report_number'])>0, listOfDicts))

     
    listOfDictsViralLineageSplitted = []

    for dt in listOfDicts:

        dt['ref_id'] = None  

        viralLineage = dt['viral_lineage']

        if viralLineage is not None:
            temp = viralLineage.strip().split(',')

            if len(temp) > 1:  
                for vl in temp:
                    dt['ref_id'] = str(uuid.uuid1()) ##nedd to "import uuid"
                    dt['viral_lineage'] = vl.strip()
                    dt['viral_name'] = vl.strip()

                    listOfDictsViralLineageSplitted.append(dt)
            else: 
                 
                dt['viral_lineage'] = viralLineage.strip()
                listOfDictsViralLineageSplitted.append(dt)
        else: 
            listOfDictsViralLineageSplitted.append(dt)


   
    bigDictOfListTuples = {}

    for dt in listOfDictsViralLineageSplitted:  

        reportNumber = dt['report_number']

        
        viral_lineage_fulltext_search = None
        viralLineage = dt['viral_lineage']

        if viralLineage is not None:
            viral_lineage_fulltext_search = viralLineage.replace('.', '_')
            
         
        dataDate = toYYYYMMDD(dt['data_date'])
         
        dataUpdatedDate = toYYYYMMDD(dt['data_updated_date'])
        
        drug_activity1_numeric_fold = dt['drug_activity1_numeric_fold']
        if len(drug_activity1_numeric_fold.strip()) <= 0:
            drug_activity1_numeric_fold = None
        
        
        sublistOfTuples = [] # key=report_number, value=sublistOfTuples
        if reportNumber in bigDictOfListTuples.keys():
            sublistOfTuples = bigDictOfListTuples[reportNumber]
                
         
        sublistOfTuples.append(
            (
            dt["data_title"],
            dt['data_source'], 
	    dt['data_source_type'],
	    dataDate, 
	    dt['assay_type'],
						   
				dt['assay_sample'],
				dt['assay_sera_time'],
				dt['assay_sera_dose'],
				dt['assay_sera_dose_unit'],
				dt['assay_cell_line'], #10
						
				dt['viral_var_ref'],
				dt['viral_type'],
				dt['viral_name'],
				dt['viral_accession_num'],
				dt['viral_lineage'], 
						
				dt['viral_protein'],
				dt['viral_protein_full_partial'],
				dt['viral_protein_backbone'],
				dt['viral_full_strain_type'],
				dt['viral_full_strain_source'], #20
						
				dt['viral_full_seq_confirmed'],
				dt['viral_aa_pos'],
				dt['viral_aa_mutation'],
				dt['drug_name'],
				dt['drug_class'], 
						 
				dt['drug_effect'],
				dt['drug_activity1_name'],
				dt['drug_activity1'],
				dt['drug_activity1_unit'],
				dt['drug_activity1_formula'], #30
   
				dt['drug_activity2_name'],
				dt['drug_activity2'],
				dt['drug_activity2_unit'],
				dt['drug_activity2_formula'],
				dt['drug_activity3_name'], 
						
				dt['drug_activity3'],
				dt['drug_activity3_unit'],
				dt['drug_activity3_formula'],
				dt['drug_notes'],
				dt['notes'], #40
						 
				dt['assay_key'], 
				reportNumber, 
				dt['data_provider'], 
						
				dt['data_source_2'], 
				dt['releasable'], 
				dt['drug_UNII'], 
						
				dt['drug_drugbankID'], 
				dt['drug_ref'], 
				dt['drug_est'], 
						 
				dt['ref_id'], #50
				dt['drug_class_sub'],
						
				dt['drug_activity1_description'],
				dt['drug_activity2_description'],
				dt['drug_activity3_description'], 
						
				dt['viral_type_sub'], 
						
				dt['activity_summary'], 
				dt['activity1_summary'],
				dt['activity2_summary'],
				dt['activity3_summary'],
						
                drug_activity1_numeric_fold,#60
				dataUpdatedDate,
		            	
		        dt['drug_sponsored'],
		        dt['viral_lineage_mod'],
		            	
		        viral_lineage_fulltext_search,

                dt['viral_lineage_full'],
                dt['drug_activity1_numeric_sign'],
                dt['activity_fold_change'],
                dt['viral_sublineage']
            )
        )

         
        bigDictOfListTuples[reportNumber] = sublistOfTuples

   
    insertSQL= """
				insert into variant3 (
				data_title, data_source,  data_source_type, 
				data_date, assay_type, assay_sample, 
				assay_sera_time,  assay_sera_dose, assay_sera_dose_unit, 
				assay_cell_line,  viral_var_ref, viral_type, 
				viral_name, viral_accession_num, viral_lineage, 
				viral_protein, viral_protein_full_partial, viral_protein_backbone, 
				viral_full_strain_type, viral_full_strain_source, viral_full_seq_confirmed, 
				viral_aa_pos, viral_aa_mutation, drug_name, 
				drug_class, drug_effect, drug_activity1_name, 
				drug_activity1, drug_activity1_unit, drug_activity1_formula, 
				drug_activity2_name, drug_activity2, drug_activity2_unit, 
				drug_activity2_formula, drug_activity3_name, drug_activity3, 
				drug_activity3_unit, drug_activity3_formula, drug_notes, 
				notes, 
				
				assay_key, report_number, data_provider, 
				data_source_2, releasable, drug_UNII, 
				drug_drugbankID, drug_ref, drug_est, 
				
				ref_id, drug_class_sub, 
				drug_activity1_description,drug_activity2_description,drug_activity3_description, 
				viral_type_sub, 
				activity_summary, activity1_summary, activity2_summary, activity3_summary,
				drug_activity1_numeric_fold,
				data_updated_date, drug_sponsored,viral_lineage_mod,viral_lineage_fulltext_search,
                viral_lineage_full, drug_activity1_numeric_sign, activity_fold_change,
                viral_sublineage
				) 
				
				values (
				%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,
				%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,  %s,%s,%s,%s,%s, 
				%s,%s,%s, %s,%s,%s, %s,%s,%s, 
				%s,%s, 
				%s,%s,%s,
				%s, 
				%s,%s,%s,%s,
				%s,
				%s,%s,%s,%s,
                %s,%s,%s,
                %s
				)
                """ 
    
    totalRec=0
    for reportNum in bigDictOfListTuples.keys():

         
        mysql = 'delete from variant3 where report_number ='+reportNum
        drugDA.runSQL(mysql)
        drugDA.runSQL('commit')
        
        insertVal = bigDictOfListTuples[reportNum]  #insertVal is list of tuples

        drugDA.runSQL('commit')
        totalRec=totalRec+len(insertVal)
        drugDA.runInsertListOfTuple(insertSQL, insertVal)
         
        drugDA.runSQL('update variant3 set date_uploaded=now() where report_number ='+reportNum)
         
        drugDA.runSQL('commit')     
    print('\n---total records were inserted into table variant3 is: '+str(totalRec)+' from file '+dataFileFullPath)
    
     
    updateViralLineageId = '''update variant3 v 
             set v.viral_meta_id = (select m.id from viral_meta m 
             where v.viral_lineage=m.viral_lineage)'''
    drugDA.runSQL(updateViralLineageId)
    drugDA.runSQL('commit') 
     
    updateVariantDrugId = '''update variant3 v 
             set v.variant_drug_id = (select d.id from variant_drug d 
             where v.drug_name=d.drug_name)'''
    drugDA.runSQL(updateVariantDrugId)
    drugDA.runSQL('commit')

    
    mysql="truncate table variant3_dataset"  
    drugDA.runSQL(mysql)
    drugDA.runSQL('commit')
     
    mysql = '''insert into  variant3_dataset 
                        (report_number, data_title, data_provider) 
                (select  report_number, data_title, data_provider from variant3 group by report_number, data_title, data_provider)
                '''
    drugDA.runSQL(mysql)
    drugDA.runSQL('commit')
     
    mysql = '''update variant3_dataset  vd
                set vd.data_date= 
                    (select max(v.data_date) from variant3 v  where v.report_number = vd.report_number group by v.report_number)
                '''

    drugDA.runSQL(mysql)
    drugDA.runSQL('commit')
     
    mysql = '''update variant3_dataset vd
                set vd.data_updated_date = 
                    (select max(v.data_updated_date) from variant3 v  where v.report_number = vd.report_number  group by v.report_number)
                '''
    drugDA.runSQL(mysql)
    drugDA.runSQL('commit')

      
    mysql = '''update variant3_dataset 
                set file_name =  
                    concat( REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(data_title,',',''),';',''),'"',''),'\'\'',''),':',''), '.tsv')
                '''
    drugDA.runSQL(mysql)
    drugDA.runSQL('commit')

     
    mysql = '''update variant3_dataset vd 
                set vd.data_source = 
                    (SELECT v.data_source
                        FROM variant3 v 
                        WHERE 
                            id IN (SELECT min(id) FROM variant3  where data_source is not null group by report_number) 
                        and v.report_number=vd.report_number
                    )
                '''
    drugDA.runSQL(mysql)
    drugDA.runSQL('commit')
     
    mysql = '''update variant3_dataset vd 
                set vd.data_source_2 = 
                    (   select 
                            SUBSTRING( GROUP_CONCAT(v.data_source2,'___'), 1, CHAR_LENGTH(GROUP_CONCAT(v.data_source2,'___'))-3 )
                        from (
                            select distinct replace(data_source_2,';','') as data_source2, report_number 
                            from variant3 group by data_source2,report_number
                        ) v 
	                    where v.report_number = vd.report_number  group by v.report_number)
                '''
    drugDA.runSQL(mysql)
    drugDA.runSQL('commit')
    

    sql_columns = 'viral_lineage_full, viral_type, viral_protein_full_partial, viral_aa_mutation, assay_type, drug_name, drug_class, activity_fold_change, activity_summary, drug_notes, viral_var_ref, drug_ref,viral_protein_backbone, viral_full_strain_type, viral_full_strain_source,data_provider, data_title, report_number, data_source, data_source_2, data_source_type,drug_activity1_name, drug_activity1, drug_activity1_unit, drug_activity2_name, drug_activity2, drug_activity2_unit, drug_activity3_name, drug_activity3,data_date, data_updated_date'
        
    file_header = sql_columns.replace('report_number','dataset_id').replace(' ','').replace(',','\t')

    formatted_sql_columns = sql_columns.replace('data_date','DATE_FORMAT(data_date, \'%m/%d/%Y\')').replace('data_updated_date','DATE_FORMAT(data_updated_date,  \'%m/%d/%Y\')')

    mysql = '''update variant3_dataset vd 
                set vd.data_clob = ( 
                    select  concat( '%s\n',  GROUP_CONCAT( CONCAT_WS('\t', %s )   SEPARATOR '\n'  ) )
                    from variant3 v
                    where 
                        v.report_number = vd.report_number  
                    group by report_number
                )
            '''%(file_header, formatted_sql_columns)

    drugDA.runSQL(mysql)
    drugDA.runSQL('commit')


    #Task 7 
    dataFileName=file7

    dataFileFullPath  = '%s/%s/%s' % (os.path.abspath('.'),'etlData',dataFileName)  
    os.system('vim +"set nobomb | set fenc=utf8 | x" '+dataFileFullPath)

    listOfDicts = []
    with open(dataFileFullPath,'r') as f: #<---first import to List Of Dict

        listOfDicts = [
            {k: v for k, v in row.items()}  
            for row in DictReader(f, skipinitialspace=True, delimiter='\t')
        ]

    insertVal=[]  

    for dt in listOfDicts:    
    
        insertVal.append((
                dt['section_id'],
                dt['section'],
                dt['section_order'],
                dt['site_title'],
                dt['site_link'],
                dt['site_description'],
                dt['display'],
                dt['display_order']
            ))

     
   
    insertSQL="INSERT INTO variant_related_resource (section_id, section, section_order, site_title, site_link, site_description, display, display_order) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

     
    mysql="truncate table variant_related_resource" #<---delete all recodrs in table variant_drug
    drugDA.runSQL(mysql) 
    drugDA.runSQL('commit')
    drugDA.runInsertListOfTuple(insertSQL, insertVal)
    drugDA.runSQL('commit')
    drugDA.runSQL('SET SQL_SAFE_UPDATES = 0')
    drugDA.runSQL('update variant_related_resource set data_uploaded_date=now();')
    drugDA.runSQL('SET SQL_SAFE_UPDATES = 1')
    drugDA.runSQL('commit')     

    print('\n---total records were inserted into table variant_related_resource is: '+str(len(insertVal))+' from file '+dataFileFullPath)
    #====================================ALL DONE=================================
    print('\n---End ETL---\n')
  
    print("Time used :", time.time() - start_time)
 
