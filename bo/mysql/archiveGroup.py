class archiveGroup:
    def __init__(self,database_name,name,eb_group_number,group_type,company_status ,domain_name,ip,days_since_created,full_name,national_producer_number,email):
        self.database_name=database_name
        self.name=name
        self.eb_group_number=eb_group_number
        self.group_type=group_type
        self.company_status=company_status
        self.domain_name=domain_name
        self.ip=ip
        self.days_since_created=days_since_created
        self.full_name=full_name
        self.national_producer_number=national_producer_number
        self.email=email


    def __str__(self):
        return "This class present archive groups for each environment which has fields:database_name,name,eb_group_number,group_type,company_status ,domain_name,ip,days_since_created,full_name,national_producer_number,email"

    def toCSV(self):
        tempStr=''
        tempStr+=self.database_name if isinstance(self.database_name,str) else str(self.database_name)
        tempStr+=' , '
        tempStr+=self.name if isinstance(self.name,str) else str(self.name)

        tempStr+=' , '
        tempStr+=self.eb_group_number if isinstance(self.eb_group_number,str) else str(self.eb_group_number)
        tempStr+=' , '
        tempStr+=self.group_type if isinstance(self.group_type,str) else str(self.group_type)
        
        tempStr+=' , '
        tempStr+=self.company_status if isinstance(self.company_status,str) else str(self.company_status)
        
        tempStr+=' , '
        tempStr+=self.domain_name if isinstance(self.domain_name,str) else str(self.domain_name)
        tempStr+=' , '
        tempStr+=self.ip if isinstance(self.ip,str) else str(self.ip)
        tempStr+=' , '
        tempStr+=self.days_since_created if isinstance(self.days_since_created ,str) else str(self.days_since_created )
        tempStr+=' , '
        tempStr+=self.full_name if isinstance(self.full_name ,str) else str(self.full_name )
        tempStr+=' , '
        tempStr+=self.national_producer_number if isinstance(self.national_producer_number ,str) else str(self.national_producer_number )
        tempStr+=' , '
        tempStr+=self.email if isinstance(self.email ,str) else str(self.email )
        return tempStr

    @classmethod
    def toTuple(self):
        return  (self.database_name,self.name,self.eb_group_number,self.group_type,self.company_status ,self.domain_name,self.ip,self.days_since_created,self.full_name,self.national_producer_number,self.email)
    @classmethod    
    def fromTuple(cls,myTuple):
        return cls(myTuple['database_name'],myTuple['name'],myTuple['eb_group_number'],myTuple['group_type'],myTuple['company_status'],myTuple['domain_name'] ,myTuple['ip'],myTuple['days_since_created'],myTuple['full_name'],myTuple['national_producer_number'],myTuple['email'])



