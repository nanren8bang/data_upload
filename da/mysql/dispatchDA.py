#import dispatchShardReport.bo.dispatch      as dispatchBO

import bo.shard      as shardBO
import bo.group      as groupBO
import da.mysqlDispatch.connectionFactory4Dispatch as CF

class dispatchDA:

    ##1: C 


    ##2: R 

    @staticmethod
    def getBOListFromSpaceSeperatedValues(myFile):
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

    @staticmethod       
    def getMasterShardList():
        myBOList=[]
        mySQL="""
                SELECT
                     id,
                     ip,
                     domain_name AS vip
                     FROM
                         `shard`
                     WHERE
                          shard_name NOT IN ('MASTER', 'DISPATCH', 'FEEDS')
          """    
        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(shardBO.shard.fromTuple(result))
        return myBOList

    @staticmethod       
    def getMasterShardListById(Id):
        myBOList=[]
        mySQL="""
                SELECT
                     id,
                     ip,
                     domain_name AS vip
                     FROM
                         `shard`
                     WHERE
                          shard_name NOT IN ('MASTER', 'DISPATCH', 'iFEEDS')
                          and id=%s
          """ %Id

        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(shardBO.shard.fromTuple(result))
        return myBOList
    @staticmethod       
    def getSlaveShardList():
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
        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(shardBO.shard.fromTuple(result))
        return myBOList

    @staticmethod       
    def getSlaveShardListById(Id):
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

        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(shardBO.shard.fromTuple(result))
        return myBOList
    
    @staticmethod       
    def getGroupListByShardId(shardId):
        myBOList=[]
        mySQL="""
              SELECT
					id AS group_id,
					database_name,
					eb_group_number,
					name,
					company_status
				FROM
					`group`
				WHERE
					shard_id = %s 
					AND database_name IS NOT NULL 
					-- group_type = 'DIRECT'
					AND group_type = 'CLIENT'
                                        AND company_status = "PRODUCTION" 
                                        AND partner_id = 2
				ORDER BY
					database_name
			""" % shardId

        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(groupBO.group.fromTuple(result))
        return myBOList
    
    @staticmethod       
    def getAllGroupList():
        myBOList=[]
        mySQL="""
              SELECT
					id AS group_id,
					database_name,
					eb_group_number,
					name,
					company_status
				FROM
					`group`
				WHERE
				        database_name IS NOT NULL 
					AND group_type = 'CLIENT'
                                        AND company_status = "PRODUCTION" 
                                        AND partner_id = 2
				ORDER BY
					database_name
			""" 

        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(groupBO.group.fromTuple(result))
        return myBOList
    
    @staticmethod       
    def getShardDBNameByEBGroupNumber(eb_group_number):
        myBOList=[]
        mySQL="select eb_group_number,shard_id,database_name  from dispatch.`group` where eb_group_number="+"'"+eb_group_number.strip()+"'" 
        #print("mySQL= "+mySQL)
        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        returnStr=""
        if results: 
            for result in results:
                returnStr=str(result['eb_group_number'])+","+str(result['shard_id'])+","+str(result['database_name'])
        return returnStr
    
    @staticmethod       
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
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory.runSQL(mySQL)
   
 

