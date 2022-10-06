import random
import string
import importlib
#import bo.report                   as reportBO
import da.oracle.connectionFactory as CF

class reportDA:

    ##1: C 


    ##2: R 

    @staticmethod
    def getReport4Table(mySQL4Report, reportList):

        results=CF.connectionFactory.runSelect1(mySQL4Report)
        reportBO=None
        reportBO=importlib.import_module('bo.report')       
        reportBO=importlib.reload(reportBO)       
        

        myBOList=[]
        if results:
            for result in results:
                myBO=None
                myBO=reportBO.report.fromTuple(result)
        
                #below is to add all shard&group infor from dispatch.group table
                #myBO.database_name=credentialBO.database_name
                myBOList.append(myBO)
        
        ##reportList.extend( myBOList)
        if  myBOList:
            reportList.extend( myBOList)
            return '__________ Got report'
        else:
            return 'No report'

    @staticmethod
    def getRecordCount(mySQL4RecordCount): # most time like "select count(*) from table where..."

        results=CF.connectionFactory.runSelect1(mySQL4RecordCount)
        if results:
            for result in results: #result is Dict , looks like {'COUNT(*)': 6612}
                return result['COUNT(*)'] # this will return int
        else:
            return None



    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    def runSQL(mySQL):
        CF.connectionFactory.runSQL(mySQL)
 

