import os
import re
import random
import string
import MySQLdb
import bo.report      as BO
import da.mysqlDispatch.connectionFactory4Shard as CF
class sqlExcutorDA:

    ##1: C 


    ##2: R 

    @staticmethod
    def runSQL4Group(credentialBO,mySQLList,reportList):

        myConnection=None
        #myConnection=CF.connectionFactory4Shard.getConnection(credentialBO.mysqlServer,credentialBO.database_name,credentialBO.mysqlUser,credentialBO.mysqlPassword)        
        myConnection=CF.connectionFactory4Shard.getConnection(credentialBO.mysqlServer,credentialBO.mysqlUser,credentialBO.mysqlPassword,credentialBO.database_name)        
        myCursor = myConnection.cursor(MySQLdb.cursors.DictCursor)
        myConnection.autocommit(True)
        sql_failure = 0

        returnString=''

        for mySQL in mySQLList:
            try:
                results=myCursor.execute(mySQL)
                #print ('In serevr %s , schem:%s , RUN %s '%(credentialBO.mysqlServer,credentialBO.database_name,mySQL))
                if results:
                   for result in results:
                       returnString=returnString+" | "+result
                
            except MySQLdb.Error as e:
                returnString=returnString+" | FAILED: In Serevr:" +credentialBO.mysqlServer+" Schema:"+credentialBO.database_name+ " Reason:" +e.args[1]+ " SQL: "+mySQL
                reportList.append(BO.report(returnString))
                myCursor.close()
                myConnection.close()
                return returnString

        myCursor.close()
        myConnection.close()

        reportList.append(BO.report(returnString))
        return 'Server %s , Schema:%s, Results:%s'%(credentialBO.mysqlServer,credentialBO.database_name,returnString)

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
 

