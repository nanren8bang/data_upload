import bo.shard         as shardBO
import da.mysqlDispatch.connectionFactory4Shard as CF
class shardDA:

    ##1: C 


    ##2: R 



    @staticmethod       
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
        results=CF.connectionFactory4Shard.runSelect(mySQL)
        for result in results:
            myBOList.append(shardBO.shard.fromTuple(result))
        return myBOList

    @staticmethod       
    def getShardListById(Id):
        myBOList=[]
        mySQL="""
                SELECT
                     id,
                     ip,
                     REPLACE(domain_name, 'master', 'slave') AS vip
                     FROM
                         `shard`
                     WHERE
                          shard_name NOT IN ('MASTER', 'DISPATCH', 'iFEEDS')
                          and id=%s
          """ %Id

        results=CF.connectionFactory4Shard.runSelect(mySQL)
        for result in results:
            myBOList.append(shardBO.shard.fromTuple(result))
        return myBOList
    
    
    @staticmethod       
    def getMaxConnection(dbServerName,myUser, myPassword):
        returnValue=0
        mySQL="""
              SHOW VARIABLES LIKE "max_connections";
          """
        #results=CF.connectionFactory4Shard.runSelect(credentialBO.mysqlServer,credentialBO.database_name,credentialBO.mysqlUser,credentialBO.mysqlPassword,mySQL)
        results=CF.connectionFactory4Shard.runSelect(dbServerName,myUser,myPassword ,mySQL,'')
        ##results is tuple , each element is dict, element looks like: {'Variable_name': 'max_connections', 'Value': '1000'}
        if results:
           returnValue=results[0]['Value']

        #for result in results:
        #    print(str(result))
        #    returtnString=returnString + str(result) 
        return returnValue

    @staticmethod       
    def getThreadsConnected(dbServerName,myUser, myPassword):
        returnValue=0
        mySQL="""
              SHOW STATUS WHERE `variable_name` = 'Threads_connected';
          """
        #results=CF.connectionFactory4Shard.runSelect(credentialBO.mysqlServer,credentialBO.database_name,credentialBO.mysqlUser,credentialBO.mysqlPassword,mySQL)
        results=CF.connectionFactory4Shard.runSelect(dbServerName,myUser,myPassword ,mySQL,'')
        ##results is tuple , each element is dict, element looks like: {'Variable_name': 'max_connections', 'Value': '1000'}
        if results:
           returnValue=results[0]['Value']

        #for result in results:
        #    print(str(result))
        #    returtnString=returnString + str(result) 
        return returnValue

    @staticmethod       
    def getAvailableConnection(dbServerName,myUser, myPassword):
        returnValue=0

        mySQL="""
              SHOW VARIABLES LIKE "max_connections";
          """
        #results=CF.connectionFactory4Shard.runSelect(credentialBO.mysqlServer,credentialBO.database_name,credentialBO.mysqlUser,credentialBO.mysqlPassword,mySQL)
        results=CF.connectionFactory4Shard.runSelect(dbServerName,myUser,myPassword ,mySQL,'')
        ##results is tuple , each element is dict, element looks like: {'Variable_name': 'max_connections', 'Value': '1000'}
        maxConnections=0

        if results:
           maxConnections=results[0]['Value']

        mySQL="""
              SHOW STATUS WHERE `variable_name` = 'Threads_connected';
          """
        #results=CF.connectionFactory4Shard.runSelect(credentialBO.mysqlServer,credentialBO.database_name,credentialBO.mysqlUser,credentialBO.mysqlPassword,mySQL)
        results=CF.connectionFactory4Shard.runSelect(dbServerName,myUser,myPassword ,mySQL,'')
        ##results is tuple , each element is dict, element looks like: {'Variable_name': 'max_connections', 'Value': '1000'}
        threadsConnected=0;
        if results:
           threadsConnected=results[0]['Value']

        #for result in results:
        #    print(str(result))
        #    returtnString=returnString + str(result) 
        return int(maxConnections)-int(threadsConnected)


    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory4Shard.runSQL(mySQL)
   
 

