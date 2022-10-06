##File          : report.py 
##Date Created  :03/18/2022, 16:08:46
##Author        : Ken Liu 
##TABLE_NAME,COLUMN_NAME,DATA_TYPE,DATA_TYPE_OWNER,DATA_LENGTH,DATA_PRECISION,DATA_SCALE,NULLABLE,COLUMN_ID,DEFAULT_LENGTH,DATA_DEFAULT

class column:
 
    def __init__(self,tablename,columnname, datatype,datatypeowner,datalength,dataprecision,datascale,nullable,columnid,defaultlength,datadefault):
        self.tablename=tablename
        self.columnname=columnname
        self.datatype=datatype
        self.datatypeowner=datatypeowner
        self.datalength=datalength
        self.dataprecision=dataprecision
        self.datascale=datascale
        self.nullable=nullable
        self.columnid=columnid
        self.defaultlength=defaultlength
        self.datadefault=datadefault

        ##beflore convert from Oracle2Postgre
        self.columnname4postgre=''
        self.datatype4postgre=''


    def __str__(self):
        return "This class hold column name and it's data type, data length...etc for each table in DB"
    
    def toCSV(self):
        tempStr=''
        tempStr+=self.tablename.strip() if isinstance(self.tablename,str) else str(self.tablename).strip()  
        tempStr+='.'
        tempStr+=self.columnname.strip() if isinstance(self.columnname,str) else str(self.columnname).strip()
        tempStr+=','
        tempStr+=self.datatype.strip() if isinstance(self.datatype,str) else str(self.datatype).strip()  
        tempStr+=','
        tempStr+=self.datalength.strip() if isinstance(self.datalength,str) else str(self.datalength).strip()  
        tempStr+=','
        tempStr+=self.nullable.strip() if isinstance(self.nullable,str) else str(self.nullable).strip()  
        tempStr+=','
        tempStr+=self.datadefault.strip() if isinstance(self.datadefault,str) else str(self.datadefault).strip()  
        tempStr+=','
        tempStr+=self.dataprecision.strip() if isinstance(self.dataprecision,str) else str(self.dataprecision).strip()  
        tempStr+=','
        tempStr+=self.datascale.strip() if isinstance(self.datascale,str) else str(self.datascale).strip()  

        tempStr+=','
        tempStr+=self.tablename.strip() if isinstance(self.tablename,str) else str(self.tablename).strip()  
        tempStr+=','
        tempStr+=self.owner.strip() if isinstance(self.owner,str) else str(self.owner).strip()  
        tempStr+='\n' 
        return tempStr
 
    def toTSV(self):
        tempStr=''
        tempStr+=self.column.strip() if isinstance(self.column,str) else str(self.column).strip()
        tempStr+='\t'
        tempStr+=self.datatype.strip() if isinstance(self.datatype,str) else str(self.datatype).strip()  
        tempStr+='\t'
        tempStr+=self.datalength.strip() if isinstance(self.datalength,str) else str(self.datalength).strip()  
        tempStr+='\t'
        tempStr+=self.nullable.strip() if isinstance(self.nullable,str) else str(self.nullable).strip()  
        tempStr+='\t'
        tempStr+=self.datadefault.strip() if isinstance(self.datadefault,str) else str(self.datadefault).strip()  
        tempStr+='\t'
        tempStr+=self.dataprecision.strip() if isinstance(self.dataprecision,str) else str(self.dataprecision).strip()  
        tempStr+='\t'
        tempStr+=self.datascale.strip() if isinstance(self.datascale,str) else str(self.datascale).strip()  
        tempStr+='\t'
        tempStr+=self.tablename.strip() if isinstance(self.tablename,str) else str(self.tablename).strip()  
        tempStr+='\t'
        tempStr+=self.owner.strip() if isinstance(self.owner,str) else str(self.owner).strip()  
        tempStr+='\n' 
        return tempStr 


    def toTuple(self):
        return (self.tablename,self.columnname, self.datatype,self.datatypeowner,self.datalength,self.dataprecision,self.datascale,self.nullable,self.columnid,self.defaultlength,self.datadefault)
    

    @classmethod
    def fromTuple(cls,myTuple):
        return cls(myTuple['TABLE_NAME'],myTuple['COLUMN_NAME'],myTuple['DATA_TYPE'],myTuple['DATA_TYPE_OWNER'],myTuple['DATA_LENGTH'],myTuple['DATA_PRECISION'],myTuple['DATA_SCALE'], myTuple['NULLABLE'],myTuple['COLUMN_ID'],myTuple['DEFAULT_LENGTH'],myTuple['DATA_DEFAULT'])

    @classmethod
    def getHeaderCSV(cls):
        return 'tablename'+','+'columnname'+','+'datatype'+','+'datatypeowner'+','+'datalength'+','+'dataprecision'+','+'datascale'+','+'nullable'+','+'columnid'+','+'defaultlength'+','+'datadefault'+'\n'
        
    @classmethod
    def getHeaderTSV(cls):
        return 'tablename'+'\t'+'columnname'+'\t'+ 'datatype'+'\t'+'datatypeowner'+'\t'+'datalength'+'\t'+'dataprecision'+'\t'+'datascale'+'\t'+'nullable'+'\t'+'columnid'+'\t'+'defaultlength'+'\t'+'datadefault'+'\n' 
