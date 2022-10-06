##File          : report.py 
##Date Created  :03/18/2022, 16:08:46
##Author        : Ken Liu 


#——how to check all constraints on a table in oracle
#https://techgoeasy.com/check-all-constraints-table-oracle/


#select TABLE_NAME,CONSTRAINT_NAME  C_NAME,INDEX_NAME,CONSTRAINT_TYPE,Search_condition,R_CONSTRAINT_NAME R_NAME from user_constraints  order by TABLE_NAME;

#select TABLE_NAME,OWNER,CONSTRAINT_NAME ,COLUMN_NAME,POSITION  from  User_cons_columns order by  TABLE_NAME;

#select uc.TABLE_NAME,uc.CONSTRAINT_NAME,uc.INDEX_NAME,uc.CONSTRAINT_TYPE,uc.Search_condition,uc.R_CONSTRAINT_NAME ,ucc.COLUMN_NAME,ucc.POSITION FROM user_constraints uc,User_cons_columns ucc Where uc.CONSTRAINT_NAME=ucc.CONSTRAINT_NAME And uc.TABLE_NAME=ucc.TABLE_NAME order by uc.TABLE_NAME;


class constraint:
 
    def __init__(self,tablename,constraintname,constrainttype, indexname,searchcondition,rconstraintname,columnname,position):
        self.tablename=tablename
        self.constraintname=constraintname
        self.constrainttype=constrainttype
        self.indexname=indexname
        self.searchcondition=searchcondition
        self.rconstraintname=rconstraintname
        self.columnname=columnname
        self.position=position


    def __str__(self):
        return "This class hold all constrain info for Oracle table like nullable, primary/foreign key, unique key ...etc"
    
    def toCSV(self):
        tempStr=''
        tempStr+=self.tablename.strip() if isinstance(self.tablename,str) else str(self.tablename).strip()  
        tempStr+='.'
        tempStr+=self.constraintname.strip() if isinstance(self.constraintname,str) else str(self.constraintname).strip()
        tempStr+=','
        tempStr+=self.constrainttype.strip() if isinstance(self.constrainttype,str) else str(self.constrainttype).strip()  
        tempStr+=','
        tempStr+=self.indexname.strip() if isinstance(self.indexname,str) else str(self.indexname).strip()  
        tempStr+=','
        tempStr+=self.searchcondition.strip() if isinstance(self.searchcondition,str) else str(self.searchcondition).strip()  
        tempStr+=','
        tempStr+=self.rconstraintname.strip() if isinstance(self.rconstraintname,str) else str(self.rconstraintname).strip()  
        tempStr+=','
        tempStr+=self.columnname.strip() if isinstance(self.columnname,str) else str(self.columnname).strip()  
        tempStr+=','
        tempStr+=self.position.strip() if isinstance(self.position,str) else str(self.position).strip()  
        tempStr+='\n' 
        return tempStr
 
    def toTSV(self):
        tempStr=''
        tempStr+=self.tablename.strip() if isinstance(self.tablename,str) else str(self.tablename).strip()  
        tempStr+='\t'
        tempStr+=self.constraintname.strip() if isinstance(self.constraintname,str) else str(self.constraintname).strip()
        tempStr+='\t'
        tempStr+=self.constrainttype.strip() if isinstance(self.constrainttype,str) else str(self.constrainttype).strip()  
        tempStr+='\t'
        tempStr+=self.indexname.strip() if isinstance(self.indexname,str) else str(self.indexname).strip()  
        tempStr+='\t'
        tempStr+=self.searchcondition.strip() if isinstance(self.searchcondition,str) else str(self.searchcondition).strip()  
        tempStr+='\t'
        tempStr+=self.rconstraintname.strip() if isinstance(self.rconstraintname,str) else str(self.rconstraintname).strip()  
        tempStr+='\t'
        tempStr+=self.columnname.strip() if isinstance(self.columnname,str) else str(self.columnname).strip()  
        tempStr+='\t'
        tempStr+=self.position.strip() if isinstance(self.position,str) else str(self.position).strip()  
        tempStr+='\n' 
        return tempStr

    def toTuple(self):
        return (self.tablename,self.constraintname ,self.constrainttype,self.indexname,self.searchcondition,self.rconstraintname,self.columnname,self.position)
    

    #select uc.TABLE_NAME,uc.CONSTRAINT_NAME,uc.INDEX_NAME,uc.CONSTRAINT_TYPE,uc.SEARCH_CONDITION,uc.R_CONSTRAINT_NAME ,ucc.COLUMN_NAME,ucc.POSITION FROM user_constraints uc,User_cons_columns ucc Where uc.CONSTRAINT_NAME=ucc.CONSTRAINT_NAME And uc.TABLE_NAME=ucc.TABLE_NAME order by uc.TABLE_NAME;
    @classmethod
    def fromTuple(cls,myTuple):
        return cls(myTuple['TABLE_NAME'],myTuple['CONSTRAINT_NAME'],myTuple['CONSTRAINT_TYPE'],myTuple['INDEX_NAME'],myTuple['SEARCH_CONDITION'],myTuple['R_CONSTRAINT_NAME'],myTuple['COLUMN_NAME'], myTuple['POSITION'])

    @classmethod
    def getHeaderCSV(cls):
        return 'tablename'+','+'constraintname'+','+'constrainttype'+','+'indexname'+','+'searchcondition'+','+'rconstraintname'+','+'columnname'+','+'position'+'\n'
        
    @classmethod
    def getHeaderTSV(cls):
        return 'tablename'+'\t'+'constraintname'+'\t'+'constrainttype'+'\t'+'indexname'+'\t'+'searchcondition'+'\t'+'rconstraintname'+'\t'+'columnname'+'\t'+'position'+'\n'
