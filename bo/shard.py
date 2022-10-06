class shard:
    def __init__(self,id,ip,vip,mysqlUser='',mysqlPassword=''):
        self.id=id
        self.ip=ip
        self.vip=vip  
        self.mysqlServerName=vip.split('.empoweredbenefits.com')[0]
        self.mysqlUser=mysqlUser
        self.mysqlPassword=mysqlPassword



    def __str__(self):
        return "This class present table shard which has fields: id,ip, vip...etc "

    def toCSV(self):
        tempStr=''
        tempStr+=self.id if isinstance(self.id,str) else str(self.id)
        tempStr+=' , '
        tempStr+=self.ip if isinstance(self.ip,str) else str(self.ip)
        tempStr+=' , '
        tempStr+=self.vip if isinstance(self.vip,str) else str(self.vip)

        tempStr+=' , '
        tempStr+=self.mysqlServerName if isinstance(self.mysqlServerName,str) else str(self.mysqlServerName)
        tempStr+=' , '
        tempStr+=self.mysqlUser if isinstance(self.mysqlUser,str) else str(self.mysqlUser)
        #tempStr+=' , '
        #tempStr+=self.mysqlPassword if isinstance(self.mysqlPassword,str) else str(self.mysqlPassword)
        return tempStr


    def toTuple(self):
        return  (self.id,self.ip,self.vip,self.mysqlServerName,self.mysqlUser)
        

    @classmethod
    def fromSpaceSeperatedValues(cls,myString):
        myList=myString.split()

        i=len(myList)-1 #last index

        if 0<=i:
           id=myList[0]
        else:
            id='N/A'
        if 1<=i:
           ip=myList[1]
        else:
            ip=''
        if 2<=i:
           vip=myList[2]
        else:
            vip=''
        return cls(id,ip,vip )

    @classmethod
    def fromTuple(cls,myTuple):

        return cls(myTuple['id'],myTuple['ip'],myTuple['vip'] )


