
import bo.constraint                as BO
import bo.fkey                      as fkeyBO
import da.oracle.connectionFactory  as CF


class constraintDA:

    ##1: C 


    ##2: R 

    @staticmethod       
    def getConstraintList4CurrentUser():
        myBOList=[]

        #below SQL use all_constraints to get ALL constrains from ALL owner/tablespace (totall 35 in probeDB)
        #mySQL="""
        #  select uc.TABLE_NAME,uc.CONSTRAINT_NAME,uc.INDEX_NAME,uc.CONSTRAINT_TYPE,uc.SEARCH_CONDITION,uc.R_CONSTRAINT_NAME ,ucc.COLUMN_NAME,ucc.POSITION FROM all_constraints uc,all_cons_columns ucc Where uc.CONSTRAINT_NAME=ucc.CONSTRAINT_NAME And uc.TABLE_NAME=ucc.TABLE_NAME and uc.OWNER=ucc.OWNER order by ucc.TABLE_NAME,ucc.POSITION
        #  """

        #below SQL use user_constraints to get ALL constrains from curret user (INFORMATICS) 
        mySQL="""
          select uc.TABLE_NAME,uc.CONSTRAINT_NAME,uc.INDEX_NAME,uc.CONSTRAINT_TYPE,uc.SEARCH_CONDITION,uc.R_CONSTRAINT_NAME ,ucc.COLUMN_NAME,ucc.POSITION FROM user_constraints uc,User_cons_columns ucc Where uc.CONSTRAINT_NAME=ucc.CONSTRAINT_NAME And uc.TABLE_NAME=ucc.TABLE_NAME and uc.OWNER=ucc.OWNER order by ucc.TABLE_NAME,ucc.POSITION
          """    
        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.constrain.fromTuple(result))
        return myBOList

    @staticmethod       
    def getConstraintListByOwnerAndConstraintType(owner,constraint_type):
        myBOList=[]

        #below SQL use all_constraints to get ALL constrains from curret user (INFORMATICS) 
        mySQL="""
          select uc.TABLE_NAME,uc.CONSTRAINT_NAME,uc.INDEX_NAME
                ,uc.CONSTRAINT_TYPE,uc.SEARCH_CONDITION
                ,uc.R_CONSTRAINT_NAME ,ucc.COLUMN_NAME,ucc.POSITION 
          FROM all_constraints uc,all_cons_columns ucc 
         Where uc.CONSTRAINT_NAME=ucc.CONSTRAINT_NAME 
           and uc.TABLE_NAME=ucc.TABLE_NAME 
           and uc.OWNER=ucc.OWNER
           and uc.owner='%s'
           and uc.constraint_type='%s' 
        Order by ucc.TABLE_NAME,ucc.POSITION
          """%(owner,constraint_type)    

        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.constrain.fromTuple(result))
        return myBOList

    # PKey is combination of two constarins "no-nullable " and "unique key"
    # Postgre will create default P key usig "tableName_"+PKey
    # you also can give it name using "ALTER TABLE myTableName ADD PKEY-Name PRIMARY KEY(column,column...) "
    # Or using the dafault nane "ALTER TABLE myTableName ADD  PRIMARY KEY(column,column...) "
    # Here we will keep using the deafult PKey
    # The PKey infor is in table all_constraints,all_cons_columns and joined with constraint_name AND owner
    # Primary key can contain more than one column, so understanding the order of the columns in the primary key is very important.This is why need         using "ORDER BY all_cons_columns.table_name, all_cons_columns.position;"

    @staticmethod       
    def getConstraintListByOwnerAndTableNameAndConstraintType(owner,table_name,constraint_type):
        myBOList=[]
        #myBOlist=BOList;

        #below SQL use all_constraints to get ALL constrains from curret user (INFORMATICS) 
        mySQL="""
          select uc.TABLE_NAME,uc.CONSTRAINT_NAME,uc.INDEX_NAME
                ,uc.CONSTRAINT_TYPE,uc.SEARCH_CONDITION
                ,uc.R_CONSTRAINT_NAME ,ucc.COLUMN_NAME,ucc.POSITION 
          FROM all_constraints uc,all_cons_columns ucc 
         Where uc.CONSTRAINT_NAME=ucc.CONSTRAINT_NAME 
           and uc.TABLE_NAME=ucc.TABLE_NAME 
           and uc.OWNER=ucc.OWNER
           and uc.owner='%s'
           and uc.table_name='%s'
           and uc.constraint_type='%s' 
        Order by ucc.TABLE_NAME,ucc.POSITION
          """%(owner,table_name,constraint_type)    

        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.constraint.fromTuple(result))
        return myBOList


    @staticmethod       
    def getFKeyListByOwnerAndTableName(owner,table_name):
        myBOList=[]
        #myBOlist=BOList;

        #below SQL use all_constraints to get ALL constrains from curret user (INFORMATICS) 
        mySQL="""
             SELECT c.constraint_name,
           l.table_name,
           l.column_name,
           r.table_name  r_table_name,
           r.column_name r_column_name
      FROM all_constraints c,
           all_cons_columns l,
           all_cons_columns r
     WHERE  c.table_name=l.table_name
           AND c.constraint_name = l.constraint_name
          AND c.r_constraint_name = r.constraint_name
          AND l.position = r.position
          AND c.constraint_type='R' AND c.owner ='%s' AND c.table_name='%s'
          """%(owner,table_name)    

        results=CF.connectionFactory.runSelect(mySQL)
        if results:
            for result in results:
                myBOList.append(fkeyBO.fkey.fromTuple(result))
        return myBOList

    
    #@staticmethod       
    #def getColumnListByTableName(myTable):

    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory.runSQL(mySQL)
   
 

