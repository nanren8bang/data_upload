
import bo.mysql.table                            as tableBO
import bo.mysql.column                           as columnBO
import da.mysql.connectionFactory  as CF
class popoDA:

    ##1: C 


    ##2: R 

    @staticmethod       
    def getTableListByDB(dbName):
        myBOList=[]

        mySQL="""
              SELECT table_name  FROM information_schema.tables WHERE table_type = 'base table' AND table_schema='%s';
          """%dbName.strip()
        #print(mySQL)    
        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(tableBO.table.fromTuple(result))
        return myBOList

    @staticmethod       
    def getTableList4CurrentUser():
        myBOList=[]
        mySQL="""
          SELECT table_name  FROM USER_TABLES order by TABLE_NAME
          """    
        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(tableBO.table.fromTuple(result))
        return myBOList
    
    @staticmethod       
    def getColumnListBySchemaTable(mySchema,myTable):
        myBOList=[]
        mySQL="select * from information_schema.columns where table_schema = '%s' and TABLE_NAME='%s' order by ordinal_position"%(mySchema.strip(), myTable.strip())

        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(columnBO.column.fromDict(result))
        return myBOList

    """
    mysql> select * from information_schema.columns limit 1\G;
*************************** 1. row ***************************
           TABLE_CATALOG: def
            TABLE_SCHEMA: information_schema
              TABLE_NAME: ALL_PLUGINS
             COLUMN_NAME: PLUGIN_NAME
        ORDINAL_POSITION: 1
          COLUMN_DEFAULT: ''
             IS_NULLABLE: NO
               DATA_TYPE: varchar
CHARACTER_MAXIMUM_LENGTH: 64
  CHARACTER_OCTET_LENGTH: 192
       NUMERIC_PRECISION: NULL
           NUMERIC_SCALE: NULL
      DATETIME_PRECISION: NULL
      CHARACTER_SET_NAME: utf8
          COLLATION_NAME: utf8_general_ci
             COLUMN_TYPE: varchar(64)
              COLUMN_KEY: 
                   EXTRA: 
              PRIVILEGES: select
          COLUMN_COMMENT: 
            IS_GENERATED: NEVER
   GENERATION_EXPRESSION: NULL
1 row in set (0.02 sec)

mysql> desc information_schema.columns;
+--------------------------+---------------------+------+-----+---------+-------+
| Field                    | Type                | Null | Key | Default | Extra |
+--------------------------+---------------------+------+-----+---------+-------+
| TABLE_CATALOG            | varchar(512)        | NO   |     |         |       |
| TABLE_SCHEMA             | varchar(64)         | NO   |     |         |       |
| TABLE_NAME               | varchar(64)         | NO   |     |         |       |
| COLUMN_NAME              | varchar(64)         | NO   |     |         |       |
| ORDINAL_POSITION         | bigint(21) unsigned | NO   |     | 0       |       |
| COLUMN_DEFAULT           | longtext            | YES  |     | NULL    |       |
| IS_NULLABLE              | varchar(3)          | NO   |     |         |       |
| DATA_TYPE                | varchar(64)         | NO   |     |         |       |
| CHARACTER_MAXIMUM_LENGTH | bigint(21) unsigned | YES  |     | NULL    |       |
| CHARACTER_OCTET_LENGTH   | bigint(21) unsigned | YES  |     | NULL    |       |
| NUMERIC_PRECISION        | bigint(21) unsigned | YES  |     | NULL    |       |
| NUMERIC_SCALE            | bigint(21) unsigned | YES  |     | NULL    |       |
| DATETIME_PRECISION       | bigint(21) unsigned | YES  |     | NULL    |       |
| CHARACTER_SET_NAME       | varchar(32)         | YES  |     | NULL    |       |
| COLLATION_NAME           | varchar(32)         | YES  |     | NULL    |       |
| COLUMN_TYPE              | longtext            | NO   |     |         |       |
| COLUMN_KEY               | varchar(3)          | NO   |     |         |       |
| EXTRA                    | varchar(30)         | NO   |     |         |       |
| PRIVILEGES               | varchar(80)         | NO   |     |         |       |
| COLUMN_COMMENT           | varchar(1024)       | NO   |     |         |       |
| IS_GENERATED             | varchar(6)          | NO   |     |         |       |
| GENERATION_EXPRESSION    | longtext            | YES  |     | NULL    |       |
+--------------------------+---------------------+------+-----+---------+-------+
22 rows in set (0.03 sec)

    """
    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory.runSQL(mySQL)
   
 

