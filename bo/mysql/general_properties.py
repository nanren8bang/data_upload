
class general_properties:
    def __init__(self,id,version,key,value,data_type,env, app,effective_date,expiration_date):
        self.id=id
        self.version=version
        self.key=key
        self.value=value
        self.data_type=data_type
        self.env=env
        self.app=app
        self.effective_date=effective_date
        self.expiration_date=expiration_date


    def __str__(self):
        return "This class present table dispatch.general_properties  in dispatch DB which has fields:id,version,key,value,data_type,env, app,effective_date,expiration_date"

    def toCSV(self):
        tempStr=''
        tempStr+=self.id if isinstance(self.id,str) else str(self.id)
        tempStr+=' , '
        tempStr+=self.version if isinstance(self.version,str) else str(self.version)

        tempStr+=' , '
        tempStr+=self.key if isinstance(self.key,str) else str(self.key)
        tempStr+=' , '
        tempStr+=self.value if isinstance(self.value,str) else str(self.value)
        
        tempStr+=' , '
        tempStr+=self.data_type if isinstance(self.data_type,str) else str(self.data_type)
        
        tempStr+=' , '
        tempStr+=self.env if isinstance(self.env,str) else str(self.env)
        tempStr+=' , '
        tempStr+=self.app if isinstance(self.app,str) else str(self.app)
        tempStr+=' , '
        tempStr+=self.effective_date if isinstance(self.effective_date,str) else str(self.effective_date)
        tempStr+=' , '
        tempStr+=self.expiration_date if isinstance(self.expiration_date,str) else str(self.expiration_date)
        return tempStr


    def toTuple(self):
        return  (self.id,self.version,self.key,self.value,self.data_type,self.env, self.app,self.effective_date,self.expiration_date)
        
    #@classmethod
    #def fromSpaceSeperatedValues(cls,myString):
    #    return cls(id,ip,vip )

    @classmethod
    def fromTuple(cls,myTuple):
        return cls(myTuple['id'],myTuple['version'],myTuple['key'],myTuple['value'],myTuple['data_type'],myTuple['env'],myTuple['app'],myTuple['effective_date'],myTuple['expiration_date'] )

    @classmethod
    def getHeaderCSV(cls):
        return  'id'+','+'version'+','+'key'+','+'value'+','+'data_type'+','+'env'+','+'app'+','+'effective_date'+','+'expiration_date'+' \n'
     
    @classmethod
    def getHeaderTSV(cls):
         return  'id'+'\t'+'version'+'\t'+'key'+'\t'+'value'+'\t'+'data_type'+'\t'+'env'+'\t'+' app'+'\t'+'effective_date'+'\t'+'expiration_date'+'\n'
 


"""
+-----------------+---------------------------------------------------------------------------------------------------+------+-----+---------+----------------+
| Field           | Type                                                                                              | Null | Key | Default | Extra          |
+-----------------+---------------------------------------------------------------------------------------------------+------+-----+---------+----------------+
| id              | int(11)                                                                                           | NO   | PRI | NULL    | auto_increment |
| version         | int(11)                                                                                           | YES  |     | NULL    |                |
| key             | varchar(250)                                                                                      | NO   | MUL | NULL    |                |
| value           | text                                                                                              | NO   |     | NULL    |                |
| data_type       | enum('STRING','INTEGER','LONG','BIGDECIMAL','BOOLEAN')                                            | NO   |     | NULL    |                |
| env             | enum('ALL','LOCAL','SBX','SBX2','DEV','DEV3','TEST','QA','SYST','AFLACTRAINING','PREPROD','PROD') | NO   |     | NULL    |                |
| app             | varchar(45)                                                                                       | YES  |     | NULL    |                |
| effective_date  | datetime                                                                                          | YES  |     | NULL    |                |
| expiration_date | datetime                                                                                          | YES  |     | NULL    |                |
+-----------------+---------------------------------------------------------------------------------------------------+------+-----+---------+----------------+
"""
