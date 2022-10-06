import dispatchShardReport.bo.group      as groupBO
import dispatchShardReport.da.mysqlDispatch.connectionFactory4Dispatch as CF
class groupDA:

    ##1: C 


    ##2: R 


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

        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(groupBO.group.fromTuple(result))
        return myBOList
    

    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory4Dispatch.runSQL(mySQL)
   
 

