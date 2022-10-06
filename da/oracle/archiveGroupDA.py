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
  
   GROUP BY g.id ORDER BY g.database_name;

	      """

        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.archiveGroup.fromTuple(result))
        return myBOList
    

    ##3: U of CRUD
    ##4: D of CRUD

    @staticmethod       
    def archiveGroup(myGroup,myUser, myPassword ):
        #myBOList=[]
        pass

    ##5: misc
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory4Dispatch.runSQL(mySQL)
   
 
"""
mysql> desc dispatch.group;
+-----------------------------+-----------------------------------------------------------------------------------------------+------+-----+--------------------+----------------+
| Field                       | Type                                                                                          | Null | Key | Default            | Extra          |
+-----------------------------+-----------------------------------------------------------------------------------------------+------+-----+--------------------+----------------+
| id                          | int(11)                                                                                       | NO   | PRI | NULL               | auto_increment |
| partner_id                  | int(11)                                                                                       | NO   | MUL | NULL               |                |
| eb_group_number             | varchar(45)                                                                                   | YES  | MUL |                    |                |
| name                        | varchar(200)                                                                                  | NO   |     | NULL               |                |
| database_name               | varchar(200)                                                                                  | YES  | UNI |                    |                |
| shard_id                    | int(1)                                                                                        | NO   | MUL | 1                  |                |
| maintenance_mode            | enum('NOT_IN_MAINTENANCE','IN_MAINTENANCE')                                                   | YES  |     | NOT_IN_MAINTENANCE |                |
| situs_state                 | char(2)                                                                                       | YES  | MUL | NULL               |                |
| status                      | enum('COMPLETE','INCOMPLETE','PROCESSING')                                                    | YES  |     | NULL               |                |
| sub_status                  | enum('IN_SETUP','COMPLETE')                                                                   | YES  |     | COMPLETE           |                |
| billing_start_date          | date                                                                                          | YES  |     | NULL               |                |
| billing_end_date            | date                                                                                          | YES  |     | NULL               |                |
| company_website_url         | varchar(200)                                                                                  | YES  |     | NULL               |                |
| company_status              | enum('TEMPLATE','TEST','DEMO','PRODUCTION','STAGING','INACTIVE')                              | NO   |     | PRODUCTION         |                |
| create_date                 | datetime                                                                                      | NO   | MUL | NULL               |                |
| create_admin_id             | int(11)                                                                                       | YES  |     | NULL               |                |
| group_type                  | enum('PROSPECT','CLIENT','DIRECT')                                                            | YES  |     | NULL               |                |
| rating_code_type            | enum('PEO','STANDARD','DUAL')                                                                 | YES  |     | STANDARD           |                |
| archived_date               | datetime                                                                                      | YES  |     | NULL               |                |
| allowed_plan_payment_method | enum('PAYROLL_DEDUCTION','DIRECT_PAY')                                                        | YES  |     | PAYROLL_DEDUCTION  |                |
| archived_database_name      | varchar(200)                                                                                  | YES  |     | NULL               |                |
| situs_zip                   | varchar(20)                                                                                   | YES  |     | NULL               |                |
| aflac_group_id              | varchar(13)                                                                                   | YES  | MUL | NULL               |                |
| aflac_group_name            | varchar(100)                                                                                  | YES  |     | NULL               |                |
| partner_account_type        | enum('PAYROLL','NONPAYROLL','UNION','ASSOCIATION','PAYROLLDIRECTBILL','DIRECT','PARTNERSHIP') | YES  |     | NULL               |                |
| import_type                 | enum('AFLAC_INDIVIDUAL','AFLAC_GROUP','SHARED_CASE')                                          | NO   |     | AFLAC_INDIVIDUAL   |                |
| is_checkout_allowed         | tinyint(1)                                                                                    | YES  |     | 1                  |                |
+-----------------------------+-----------------------------------------------------------------------------------------------+------+-----+--------------------+----------------+
27 rows in set (0.04 sec)

mysql> desc dispatch.shard;
+--------------+----------------------------------------------------------------------------------------------+------+-----+---------+----------------+
| Field        | Type                                                                                         | Null | Key | Default | Extra          |
+--------------+----------------------------------------------------------------------------------------------+------+-----+---------+----------------+
| id           | int(11)                                                                                      | NO   | PRI | NULL    | auto_increment |
| shard_name   | varchar(200)                                                                                 | NO   | UNI | NULL    |                |
| domain_name  | varchar(253) <---shard DNS name like sdb102.mp.qa.clt4.empoweredbenefits.com                 | YES  |     | NULL    |                |
| ip           | varchar(15)  <---Shard IP like 10.11.5.66                                                    | NO   |     | NULL    |                |
| group_count  | int(11)                                                                                      | NO   |     | NULL    |                |
| group_limit  | int(11)                                                                                      | NO   |     | NULL    |                |
| status       | enum('ACTIVE_READY','ACTIVE_STAGING','ACTIVE_LOCKED','ACTIVE_WRITE','MAINTENANCE','ARCHIVE') | NO   |     | NULL    |                |
| company_size | varchar(250)                                                                                 | NO   |     | NULL    |                |
+--------------+----------------------------------------------------------------------------------------------+------+-----+---------+----------------+
8 rows in set (0.04 sec)

"""
