import bo.archiveGroup      as BO
import da.mysqlDispatch.connectionFactory4Dispatch as CF
class archiveGroupDA:

    ##1: C 


    ##2: R 


    @staticmethod       
    def getArchiveGroups():
        myBOList=[]
        mySQL="""
              SELECT  g.database_name
      , g.name
      , IF(g.eb_group_number IS NULL,'UNDEFINED',g.eb_group_number) eb_group_number
      , IF(g.group_type IS NULL,'NULL', g.group_type) group_type
      , g.company_status 
      , s.domain_name
      , s.ip
      , (TO_DAYS(NOW())-TO_DAYS(g.create_date)) AS days_since_created
      , CONCAT(IF(a.last_name IS NULL,'',a.last_name),', ', IF(a.first_name IS NULL,'',a.first_name)) full_name
      , IF(a.national_producer_number IS NULL, 'NULL', a.national_producer_number) national_producer_number
      , IF(a.email IS NULL,'NULL',a.email) email

FROM (dispatch.group g, dispatch.shard s) 
LEFT JOIN dispatch.admin_group ag 
       ON (ag.group_id=g.id AND ag.is_owner AND ag.inactivation_date IS NULL AND ag.rejected_date IS NULL) 
LEFT JOIN dispatch.admin a 
       ON (a.id=ag.admin_id AND a.is_broker)

WHERE database_name IS NOT NULL 
  AND database_name!='' 
  AND s.id=g.shard_id 
  AND database_name NOT LIKE 'grp_loadtest%'
  AND (eb_group_number IS NULL OR (eb_group_number IS NOT NULL AND  eb_group_number NOT IN ('monitor')))
  AND (a.email IS NULL OR a.email NOT IN ('MTaylor2\@aflac.com', 'TALSOBROOK\@AFLAC.COM'))
  

  GROUP BY g.id ORDER BY g.database_name

  limit 10
	      """

        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.archiveGroup.fromTuple(result))
        return myBOList
    

    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory4Dispatch.runSQL(mySQL)
   
 

