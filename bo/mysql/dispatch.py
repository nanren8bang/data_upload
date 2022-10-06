class dispatch:
    def __init__(self,id,ip,vip):
        self.id=id
        self.ip=ip
        self.vip=vip  

    def __str__(self):
        return f"This class present table shard which has fields: id,ip, vip...etc "

    def toCSV(self):
        tempStr=''
        tempStr+=self.id if isinstance(self.id,str) else str(self.id)
        tempStr+=' , '
        tempStr+=self.ip if isinstance(self.ip,str) else str(self.ip)
        tempStr+=' , '
        tempStr+=self.vip if isinstance(self.vip,str) else str(self.vip)

        return tempStr


    def toTuple(self):
        return  (self.id,self.ip,self.vip)
        

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
        '''
        i=len(myTuple)-1 #last index

        if 0<=i:  
           id=myTuple[0]
        else:
            id=''
        if 1<=i:
           ip=myTuple[1]
        else:
            ip=''
        if 2<=i:
           vip=myTuple[2]
        else:
            vip=''
        '''

        return cls(myTuple['id'],myTuple['ip'],myTuple['vip'] )


