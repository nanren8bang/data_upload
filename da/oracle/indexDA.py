
import bo.index                     as BO
import da.oracle.connectionFactory  as CF


class indexDA:

    ##1: C 


    ##2: R 

    @staticmethod       
    def getIndexListByOwnerAndTableName(owner,table_name):
        myBOList=[]
        #——how to check all index in a table in oracle
        #https://dataedo.com/kb/query/oracle/list-table-indexes

        mySQL="""
              select ind.table_owner,
       ind.table_name,
       ind.index_name,
       LISTAGG(ind_col.column_name, ',')
            WITHIN GROUP(order by ind_col.column_position) as column_name,
       ind.index_type,
       ind.uniqueness
from sys.all_indexes ind
join sys.all_ind_columns ind_col
           on ind.owner = ind_col.index_owner
           and ind.index_name = ind_col.index_name
where ind.table_owner not in ('ANONYMOUS','CTXSYS','DBSNMP','EXFSYS',
       'MDSYS', 'MGMT_VIEW','OLAPSYS','OWBSYS','ORDPLUGINS', 'ORDSYS',
       'SI_INFORMTN_SCHEMA','SYS','SYSMAN','SYSTEM', 'TSMSYS','WK_TEST',
       'WKPROXY','WMSYS','XDB','APEX_040000','APEX_040200',
       'DIP', 'FLOWS_30000','FLOWS_FILES','MDDATA', 'ORACLE_OCM', 'XS$NULL',
       'SPATIAL_CSW_ADMIN_USR', 'SPATIAL_WFS_ADMIN_USR', 'PUBLIC',
       'LBACSYS', 'OUTLN', 'WKSYS', 'APEX_PUBLIC_USER')
     AND ind.table_owner='%s'
     AND ind.table_name='%s'
group by ind.table_owner,
         ind.table_name,
         ind.index_name,
         ind.index_type,
         ind.uniqueness 
order by ind.table_owner,
         ind.table_name

          """%(owner,table_name)    

        results=CF.connectionFactory.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.index.fromTuple(result))
        return myBOList


    #@staticmethod       
    #def getColumnListByTableName(myTable):

    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory.runSQL(mySQL)
   
 

