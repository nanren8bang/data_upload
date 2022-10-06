import random
import string
import MySQLdb
import bo.report      as BO
import da.mysqlDispatch.connectionFactory4Shard as CF
class reportDA:

    ##1: C 


    ##2: R 

    @staticmethod
    def getReport4Group(credentialBO,mySQL4Report, reportList):
   

        results=CF.connectionFactory4Shard.runSelect(credentialBO.mysqlServer,credentialBO.mysqlUser,credentialBO.mysqlPassword,mySQL4Report,credentialBO.database_name)
        
        myBOList=[]
        if results:
            for result in results:
                myBO=BO.report.fromTuple(result)
        
                #below is to add all shard&group infor from dispatch.group table
                myBO.database_name=credentialBO.database_name
                myBO.group_id=credentialBO.group_id
                myBO.group_name=credentialBO.name
                myBO.eb_group_number=credentialBO.eb_group_number

                myBOList.append(myBO)
        
        ##reportList.extend( myBOList)
        if  myBOList:
            reportList.extend( myBOList)
            return '__________ Got report'
        else:
            return 'No report'

    '''

    @staticmethod
    def getBiOListFromSpaceSeperatedValues(myFile):
        file = open(myFile, 'r')
        myBOList = []
        count=0
        while True:
            count += 1
            # Get next line from file
            line = file.readline()
 
            # if line is empty,end of file is reached
            if not line:
               break
            #print("Line{}: {}".format(count, line.strip()))  #for debug
            myBOList.append(BO.variant_drug.fromSpaceSeperatedValues(line))

        file.close() 
        return myBOList

    @staticmethod       
    def getBOListFromDB(selectStatement):
        myBOList=[]
        results=CF.connectionFactory.runSelect(selectStatement)
        for result in results:
            myBOList.append(BO.dispatch.fromTuple(result))
        return myBOList


    def getShardList():
        myBOList=[]
        mySQL="""
                SELECT
                     id,
                     ip,
                     REPLACE(domain_name, 'master', 'slave') AS vip
                     FROM
                         `shard`
                     WHERE
                          shard_name NOT IN ('MASTER', 'DISPATCH', 'FEEDS')
          """    
        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.dispatch.fromTuple(result))
        return myBOList
    
    def getNumRegistered():

        mySQL = """
                    SELECT COUNT(cg.member_id) AS count
                    FROM dispatch.credential c
                    LEFT JOIN dispatch.credential_group cg ON cg.credential_id = c.id
                    WHERE cg.is_active = 1
                       AND cg.effective_date <= CURDATE()
    
	               AND (cg.expiration_date IS NULL OR cg.expiration_date >= CURDATE())
                       AND c.is_active = 1
                       AND c.effective_date <= CURDATE()
                       AND (c.expiration_date IS NULL OR c.expiration_date >= CURDATE())
                       AND c.verified_email IS NOT NULL
                       AND c.verified_email != ""
                       AND c.consent_acceptance_date IS NOT NULL;
	        		""" 
	       
        data1  = CF.connectionFactory.runSelect(mySQL)
        
        num_registered=0
        for count in data1:
           num_registered += count['count']
        return num_registered


    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    def runSQL(mySQL):
        CF.connectionFactory.runSQL(mySQL)
   '''
 

