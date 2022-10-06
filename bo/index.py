##File          : report.py 
##Date Created  :03/18/2022, 16:08:46
##Author        : Ken Liu 


#——how to check all index in a table in oracle
#https://dataedo.com/kb/query/oracle/list-table-indexes
#A. Tables accessible to the current user
"""
#select ind.table_owner || '.' || ind.table_name as "TABLE",
select ind.table_owner,
       ind.table_name,
       ind.index_name,
       LISTAGG(ind_col.column_name, ',')
            WITHIN GROUP(order by ind_col.column_position) as column_name,
       ind.index_type,
       ind.uniqueness
from sys.all_indexes ind
join sys.all_ind_columns ind_col
           on ind.owner = ind_col.index_owner
           and ind.index_name = ind_col.index_name
where ind.table_owner not in ('ANONYMOUS','CTXSYS','DBSNMP','EXFSYS',
       'MDSYS', 'MGMT_VIEW','OLAPSYS','OWBSYS','ORDPLUGINS', 'ORDSYS',
       'SI_INFORMTN_SCHEMA','SYS','SYSMAN','SYSTEM', 'TSMSYS','WK_TEST',
       'WKPROXY','WMSYS','XDB','APEX_040000','APEX_040200',
       'DIP', 'FLOWS_30000','FLOWS_FILES','MDDATA', 'ORACLE_OCM', 'XS$NULL',
       'SPATIAL_CSW_ADMIN_USR', 'SPATIAL_WFS_ADMIN_USR', 'PUBLIC',
       'LBACSYS', 'OUTLN', 'WKSYS', 'APEX_PUBLIC_USER')
group by ind.table_owner,
         ind.table_name,
         ind.index_name,
         ind.index_type,
         ind.uniqueness 
order by ind.table_owner,
         ind.table_name;
"""
## IF you have privilege to access dba_indexes and dba_ind_columns, jist replace them in above SQL

class index:
 
    def __init__(self,table_owner,table_name,index_name,column_name,index_type,uniqueness):
        self.table_owner=table_owner
        self.table_name=table_name
        self.index_name=index_name 
        self.column_name=column_name
        self.index_type=index_type
        self.uniqueness=uniqueness


    def __str__(self):
        return "This class hold all index info for Oracle table "
    
    def toCSV(self):
        tempStr=''
        tempStr+=self.table_owner.strip() if isinstance(self.table_owner,str) else str(self.table_owner).strip()  
        tempStr+='.'
        tempStr+=self.table_name.strip() if isinstance(self.table_name,str) else str(self.table_name).strip()
        tempStr+=','
        tempStr+=self.index_name.strip() if isinstance(self.index_name,str) else str(self.index_name).strip()  
        tempStr+=','
        tempStr+=self.column_name.strip() if isinstance(self.column_name,str) else str(self.column_name).strip()  
        tempStr+=','
        tempStr+=self.index_type.strip() if isinstance(self.index_type,str) else str(self.index_type).strip()  
        tempStr+=','
        tempStr+=self.uniqueness.strip() if isinstance(self.uniqueness,str) else str(self.uniqueness).strip()  
        tempStr+='\n' 
        return tempStr
 
    def toTSV(self):
        tempStr=''
        tempStr+=self.table_owner.strip() if isinstance(self.table_owner,str) else str(self.table_owner).strip()  
        tempStr+='\t'
        tempStr+=self.table_name.strip() if isinstance(self.table_name,str) else str(self.table_name).strip()
        tempStr+='\t'
        tempStr+=self.index_name.strip() if isinstance(self.index_name,str) else str(self.index_name).strip()  
        tempStr+='\t'
        tempStr+=self.column_name.strip() if isinstance(self.column_name,str) else str(self.column_name).strip()  
        tempStr+='\t'
        tempStr+=self.index_type.strip() if isinstance(self.index_type,str) else str(self.index_type).strip()  
        tempStr+='\t'
        tempStr+=self.uniqueness.strip() if isinstance(self.uniqueness,str) else str(self.uniqueness).strip()  
        tempStr+='\n' 
        return tempStr

    def toTuple(self):
        return (self.table_owner,self.table_name,self.index_name,self.column_name,self.index_type,self.uniqueness)
    

    @classmethod
    def fromTuple(cls,myTuple):
        return cls(myTuple['TABLE_OWNER'],myTuple['TABLE_NAME'],myTuple['INDEX_NAME'],myTuple['COLUMN_NAME'],myTuple['INDEX_TYPE'],myTuple['UNIQUENESS'])

    @classmethod
    def getHeaderCSV(cls):
        return 'table_owner'+','+'table_name'+','+'index_name'+','+'column_name'+','+'index_type'+','+'uniqueness'+'\n'
        
    @classmethod
    def getHeaderTSV(cls):
        return 'table_owner'+'\t'+'table_name'+'\t'+'index_name'+'\t'+'column_name'+'\t'+'index_type'+'\t'+'uniqueness'+'\n'
