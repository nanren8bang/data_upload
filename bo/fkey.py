##File          : report.py 
##Date Created  :03/18/2022, 16:08:46
##Author        : Ken Liu 


#——how to check forign key  a table in oracle
#https://dba.stackexchange.com/questions/11047/how-to-retrieve-foreign-key-constraints-data
#Here is the one I use:

#SELECT c.constraint_name,
#           l.table_name,
#           l.column_name,
#           r.table_namei r_table_name,
#           r.column_name r_column_name
#      FROM all_constraints c,
#           all_cons_columns l,
#           all_cons_columns r
#     WHERE  c.table_name=l.table_name
#           AND c.constraint_name = l.constraint_name
#          AND c.r_constraint_name = r.constraint_name
#          AND l.position = r.position
#         AND c.owner = 'INFORMATICS'
#          and c.table_name='METADATA_FILE';  


class fkey:
 
    def __init__(self,constraintname,tablename,columnname,rtablename,rcolumnname):
        self.constraintname=constraintname
        self.tablename=tablename
        self.columnname=columnname 
        self.rtablename=rtablename
        self.rcolumnname=rcolumnname


    def __str__(self):
        return "This class hold Foreign key infor  like table name , xcolumn name ...etc"
    
    def toCSV(self):
        tempStr=''
        tempStr+=self.constraintname.strip() if isinstance(self.constraintname,str) else str(self.constraintname).strip()
        tempStr+='.'
        tempStr+=self.tablename.strip() if isinstance(self.tablename,str) else str(self.tablename).strip()
        tempStr+=','
        tempStr+=self.columnname.strip() if isinstance(self.columnname,str) else str(self.columnname).strip()  
        tempStr+=','
        tempStr+=self.rtablename.strip() if isinstance(self.rtablename,str) else str(self.rtablename).strip()
        tempStr+=','
        tempStr+=self.rcolumnname.strip() if isinstance(self.rcolumnname,str) else str(self.rcolumnname).strip()  
        tempStr+='\n' 
        return tempStr
 
    def toTSV(self):
        tempStr=''
        tempStr+=self.constraintname.strip() if isinstance(self.constraintname,str) else str(self.constraintname).strip()
        tempStr+='\t'
        tempStr+=self.tablename.strip() if isinstance(self.tablename,str) else str(self.tablename).strip()
        tempStr+='\t'
        tempStr+=self.columnname.strip() if isinstance(self.columnname,str) else str(self.columnname).strip()  
        tempStr+='\t'
        tempStr+=self.rtablename.strip() if isinstance(self.rtablename,str) else str(self.rtablename).strip()
        tempStr+='\t'
        tempStr+=self.rcolumnname.strip() if isinstance(self.rcolumnname,str) else str(self.rcolumnname).strip()  
        tempStr+='\n' 
        return tempStr

    def toTuple(self):
        return (self.constraintname ,self.tablename,self.columnname,self.rtablename,self.rcolumnname)
    @classmethod
    def fromTuple(cls,myTuple):
        return cls(myTuple['CONSTRAINT_NAME'],myTuple['TABLE_NAME'],myTuple['COLUMN_NAME'],myTuple['R_TABLE_NAME'],myTuple['R_COLUMN_NAME'])

    @classmethod
    def getHeaderCSV(cls):
        return 'constraintname'+','+'tablename'+','+'columnname'+','+'rtablename'+','+'rcolumnname'+'\n'
        
    @classmethod
    def getHeaderTSV(cls):
        return 'constraintname'+'\t'+'tablename'+'\t'+'columnname'+'\t'+'rtablename'+'\t'+'rcolumnname'+'\n'

