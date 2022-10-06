
import bo.table                            as tableBO
import bo.column                           as columnBO
import da.oracle.connectionFactory  as CF
class popoDA:

    ##1: C 


    ##2: R 

    @staticmethod       
    def getTableListByOwner(owner):
        myBOList=[]

        mySQL="""
          SELECT table_name  
          FROM ALL_TABLES
          where OWNER='%s' 
          order by TABLE_NAME
          """%owner
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
    def getColumnListByTableName(myTable):
        myBOList=[]
        #mySQL="SELECT COLUMN_NAME,DATA_TYPE FROM COLS WHERE TABLE_NAME='"+myTable.strip()+"'" 
        #mySQL="select column_name, data_type,data_length from cols where table_name='"+myTable.strip()+"'" 

        mySQL="SELECT TABLE_NAME,COLUMN_NAME,DATA_TYPE,DATA_TYPE_OWNER,DATA_LENGTH,DATA_PRECISION,DATA_SCALE,NULLABLE,COLUMN_ID,DEFAULT_LENGTH,DATA_DEFAULT from cols where TABLE_NAME='"+myTable.strip()+"'"+" order by COLUMN_ID"

        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(columnBO.column.fromTuple(result))
        return myBOList

    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory.runSQL(mySQL)
   
 

