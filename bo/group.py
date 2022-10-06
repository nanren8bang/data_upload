class group:
    def __init__(self,group_id,database_name,eb_group_number,name,company_status,mysqlServer='',mysqlUser='',mysqlPassword=''):
        self.group_id=group_id
        self.database_name=database_name
        self.eb_group_number=eb_group_number
        self.name=name
        self.company_status=company_status  
        #below files for login 
        self.mysqlServer=mysqlServer
        self.mysqlUser=mysqlUser
        self.mysqlPassword=mysqlPassword

    def __str__(self):
        return "This class present table group for each shard which has fields:group_id,database_name,eb_group_number,name,company_status..etc"

    def toCSV(self):
        tempStr=''
        tempStr+=self.group_id if isinstance(self.group_id,str) else str(self.group_id)
        tempStr+=' , '
        tempStr+=self.eb_group_number if isinstance(self.eb_group_number,str) else str(self.eb_group_number)

        tempStr+=' , '
        tempStr+=self.name if isinstance(self.name,str) else str(self.name)
        tempStr+=' , '
        tempStr+=self.company_status if isinstance(self.company_status,str) else str(self.company_status)
        
        tempStr+=' , '
        tempStr+=self.mysqlServer if isinstance(self.mysqlServer,str) else str(self.mysqlServer)
        
        tempStr+=' , '
        tempStr+=self.database_name if isinstance(self.database_name,str) else str(self.database_name)
        tempStr+=' , '
        tempStr+=self.mysqlUser if isinstance(self.mysqlUser,str) else str(self.mysqlUser)
        tempStr+=' , '
        tempStr+='******'
        #tempStr+=self.mysqlPassword  if isinstance(self.mysqlPassword ,str) else str(self.mysqlPassword)
        return tempStr


    def toTuple(self):
        return  (self.group_id,self.database_name,self.eb_group_number,self.name,self.company_status)
        

    @classmethod
    def fromTuple(cls,myTuple):
        return cls(myTuple['group_id'],myTuple['database_name'],myTuple['eb_group_number'],myTuple['name'],myTuple['company_status'] )



