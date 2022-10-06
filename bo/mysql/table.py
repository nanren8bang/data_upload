##File          : report.py 
##Date Created  :03/18/2022, 16:08:46
##Author        : Ken Liu 


class table:
    def __init__(self,table):
        self.table=table
        
    def __str__(self):
        return 'This class hold all tables for current user in DB'
    
    def toCSV(self):
        tempStr=''
        tempStr+=self.table.strip() if isinstance(self.table,str) else str(self.table).strip()
        tempStr+='\n' 
        return tempStr 
    def toTSV(self):
        tempStr=''
        tempStr+=self.table.strip() if isinstance(self.table,str) else str(self.table).strip()
        tempStr+='\n' 
        return tempStr 
    def toTuple(self):
        return (self.table)
    @classmethod
    def fromTuple(cls,myTuple):
        return cls(myTuple['table_name'])  #<--In Oracle, column name is UPCASE 
        #return cls(myTuple['table_name']) #<--In Oracle, column name is UPCASE 
    @classmethod
    def getHeaderCSV(cls):
        return 'table'+'\n'
    @classmethod
    def getHeaderTSV(cls):
        return 'table'+'\n'
