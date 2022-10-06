##File          : variant_drug.py 
##Date Created  : 05/05/2022, 19:48:22
##Author        : Ken Liu 

from typing     import List, Optional,Any  
from pydantic   import BaseModel,ValidationError,validator   

class variant_drug(BaseModel):
    id: Any
    drug_name: Any
    drug_class: Any
    priority: Any
    alias1: Any
    alias2: Any
    alias3: Any
    alias4: Any
    alias5: Any
    unii: Any
    cas: Any
    date_updated: Any
    drug_company: Any

    def __init__(self,id,drug_name,drug_class,priority,alias1,alias2,alias3,alias4,alias5,unii,cas,date_updated,drug_company ):
        super().__init__(id=id,drug_name=drug_name,drug_class=drug_class,priority=priority,alias1=alias1,alias2=alias2,alias3=alias3,alias4=alias4,alias5=alias5,unii=unii,cas=cas,date_updated=date_updated,drug_company=drug_company)

    def __str__(self):
        return 'This class hold report detail values:id,drug_name,drug_class,priority,alias1,alias2,alias3,alias4,alias5,unii,cas,date_updated,drug_company'

    def toCSV(self):
        tempStr=''
        tempStr+="'"+self.id.strip()+"'" if isinstance(self.id,str) else str(self.id).strip()
        tempStr+=','
        tempStr+="'"+self.drug_name.strip()+"'" if isinstance(self.drug_name,str) else str(self.drug_name).strip()
        tempStr+=','
        tempStr+="'"+self.drug_class.strip()+"'" if isinstance(self.drug_class,str) else str(self.drug_class).strip()
        tempStr+=','
        tempStr+="'"+self.priority.strip()+"'" if isinstance(self.priority,str) else str(self.priority).strip()
        tempStr+=','
        tempStr+="'"+self.alias1.strip()+"'" if isinstance(self.alias1,str) else str(self.alias1).strip()
        tempStr+=','
        tempStr+="'"+self.alias2.strip()+"'" if isinstance(self.alias2,str) else str(self.alias2).strip()
        tempStr+=','
        tempStr+="'"+self.alias3.strip()+"'" if isinstance(self.alias3,str) else str(self.alias3).strip()
        tempStr+=','
        tempStr+="'"+self.alias4.strip()+"'" if isinstance(self.alias4,str) else str(self.alias4).strip()
        tempStr+=','
        tempStr+="'"+self.alias5.strip()+"'" if isinstance(self.alias5,str) else str(self.alias5).strip()
        tempStr+=','
        tempStr+="'"+self.unii.strip()+"'" if isinstance(self.unii,str) else str(self.unii).strip()
        tempStr+=','
        tempStr+="'"+self.cas.strip()+"'" if isinstance(self.cas,str) else str(self.cas).strip()
        tempStr+=','
        tempStr+="'"+self.date_updated.strip()+"'" if isinstance(self.date_updated,str) else str(self.date_updated).strip()
        tempStr+=','
        tempStr+="'"+self.drug_company.strip()+"'" if isinstance(self.drug_company,str) else str(self.drug_company).strip()
        #tempStr+='\n' 
        return tempStr 

    def toTSV(self):
        tempStr=''
        tempStr+=self.id.strip() if isinstance(self.id,str) else str(self.id).strip()
        tempStr+='\t'
        tempStr+=self.drug_name.strip() if isinstance(self.drug_name,str) else str(self.drug_name).strip()
        tempStr+='\t'
        tempStr+=self.drug_class.strip() if isinstance(self.drug_class,str) else str(self.drug_class).strip()
        tempStr+='\t'
        tempStr+=self.priority.strip() if isinstance(self.priority,str) else str(self.priority).strip()
        tempStr+='\t'
        tempStr+=self.alias1.strip() if isinstance(self.alias1,str) else str(self.alias1).strip()
        tempStr+='\t'
        tempStr+=self.alias2.strip() if isinstance(self.alias2,str) else str(self.alias2).strip()
        tempStr+='\t'
        tempStr+=self.alias3.strip() if isinstance(self.alias3,str) else str(self.alias3).strip()
        tempStr+='\t'
        tempStr+=self.alias4.strip() if isinstance(self.alias4,str) else str(self.alias4).strip()
        tempStr+='\t'
        tempStr+=self.alias5.strip() if isinstance(self.alias5,str) else str(self.alias5).strip()
        tempStr+='\t'
        tempStr+=self.unii.strip() if isinstance(self.unii,str) else str(self.unii).strip()
        tempStr+='\t'
        tempStr+=self.cas.strip() if isinstance(self.cas,str) else str(self.cas).strip()
        tempStr+='\t'
        tempStr+=self.date_updated.strip() if isinstance(self.date_updated,str) else str(self.date_updated).strip()
        tempStr+='\t'
        tempStr+=self.drug_company.strip() if isinstance(self.drug_company,str) else str(self.drug_company).strip()
        tempStr+='\n' 
        return tempStr 

    def toTuple(self):
        return (self.id,self.drug_name,self.drug_class,self.priority,self.alias1,self.alias2,self.alias3,self.alias4,self.alias5,self.unii,self.cas,self.date_updated,self.drug_company)
    @classmethod
    def fromDict(cls,myDict):
        return cls(myDict['id'],myDict['drug_name'],myDict['drug_class'],myDict['priority'],myDict['alias1'],myDict['alias2'],myDict['alias3'],myDict['alias4'],myDict['alias5'],myDict['unii'],myDict['cas'],myDict['date_updated'],myDict['drug_company'])

    @classmethod
    def getHeaderCSV(cls):
        return 'id'+','+'drug_name'+','+'drug_class'+','+'priority'+','+'alias1'+','+'alias2'+','+'alias3'+','+'alias4'+','+'alias5'+','+'unii'+','+'cas'+','+'date_updated'+','+'drug_company'+','+'database_name'+','+'group_name'+','+'eb_group_number'+'\n'

    @classmethod
    def getHeaderTSV(cls):
        return 'id'+'\t'+'drug_name'+'\t'+'drug_class'+'\t'+'priority'+'\t'+'alias1'+'\t'+'alias2'+'\t'+'alias3'+'\t'+'alias4'+'\t'+'alias5'+'\t'+'unii'+'\t'+'cas'+'\t'+'date_updated'+'\t'+'drug_company'+'\t'+'database_name'+'\t'+'group_name'+'\t'+'eb_group_number'+'\n'

