##File          : report.py 
##Date Created  : 05/02/2022, 07:44:27
##Author        : Ken Liu 

from typing     import List, Optional,Any  
from pydantic   import BaseModel,ValidationError,validator   

class report(BaseModel):
    ID: Any
    SAMPLE_ID: Any
    REAGENT_NAME: Any
    REAGENT_COMMON_NAME: Any
    REAGENT_CLASS: Any
    REAGENT_SOURCE: Any
    REAGENT_LOT: Any
    REAGENT_TITER: Any
    REAGENT_AC50_UNIT: Any
    REAGENT_CAS: Any
    REAGENT_SMILES: Any
    REAGENT_LINK: Any
    REAGENT_ASSAYS: Any
    REAGENT_CONCENTRATION: Any
    REAGENT_MOLECULAR_WEIGHT: Any
    REAGENT_SHOW_HIDE: Any
    REAGENT_MOA: Any

    def __init__(self,ID,SAMPLE_ID,REAGENT_NAME,REAGENT_COMMON_NAME,REAGENT_CLASS,REAGENT_SOURCE,REAGENT_LOT,REAGENT_TITER,REAGENT_AC50_UNIT,REAGENT_CAS,REAGENT_SMILES,REAGENT_LINK,REAGENT_ASSAYS,REAGENT_CONCENTRATION,REAGENT_MOLECULAR_WEIGHT,REAGENT_SHOW_HIDE,REAGENT_MOA ):
        super().__init__(ID=ID,SAMPLE_ID=SAMPLE_ID,REAGENT_NAME=REAGENT_NAME,REAGENT_COMMON_NAME=REAGENT_COMMON_NAME,REAGENT_CLASS=REAGENT_CLASS,REAGENT_SOURCE=REAGENT_SOURCE,REAGENT_LOT=REAGENT_LOT,REAGENT_TITER=REAGENT_TITER,REAGENT_AC50_UNIT=REAGENT_AC50_UNIT,REAGENT_CAS=REAGENT_CAS,REAGENT_SMILES=REAGENT_SMILES,REAGENT_LINK=REAGENT_LINK,REAGENT_ASSAYS=REAGENT_ASSAYS,REAGENT_CONCENTRATION=REAGENT_CONCENTRATION,REAGENT_MOLECULAR_WEIGHT=REAGENT_MOLECULAR_WEIGHT,REAGENT_SHOW_HIDE=REAGENT_SHOW_HIDE,REAGENT_MOA=REAGENT_MOA)

    def __str__(self):
        return 'This class hold report detail values:ID,SAMPLE_ID,REAGENT_NAME,REAGENT_COMMON_NAME,REAGENT_CLASS,REAGENT_SOURCE,REAGENT_LOT,REAGENT_TITER,REAGENT_AC50_UNIT,REAGENT_CAS,REAGENT_SMILES,REAGENT_LINK,REAGENT_ASSAYS,REAGENT_CONCENTRATION,REAGENT_MOLECULAR_WEIGHT,REAGENT_SHOW_HIDE,REAGENT_MOA'

    def toCSV(self):
        tempStr=''
        tempStr+=self.ID.strip() if isinstance(self.ID,str) else str(self.ID).strip()
        tempStr+=','
        tempStr+=self.SAMPLE_ID.strip() if isinstance(self.SAMPLE_ID,str) else str(self.SAMPLE_ID).strip()
        tempStr+=','
        tempStr+=self.REAGENT_NAME.strip() if isinstance(self.REAGENT_NAME,str) else str(self.REAGENT_NAME).strip()
        tempStr+=','
        tempStr+=self.REAGENT_COMMON_NAME.strip() if isinstance(self.REAGENT_COMMON_NAME,str) else str(self.REAGENT_COMMON_NAME).strip()
        tempStr+=','
        tempStr+=self.REAGENT_CLASS.strip() if isinstance(self.REAGENT_CLASS,str) else str(self.REAGENT_CLASS).strip()
        tempStr+=','
        tempStr+=self.REAGENT_SOURCE.strip() if isinstance(self.REAGENT_SOURCE,str) else str(self.REAGENT_SOURCE).strip()
        tempStr+=','
        tempStr+=self.REAGENT_LOT.strip() if isinstance(self.REAGENT_LOT,str) else str(self.REAGENT_LOT).strip()
        tempStr+=','
        tempStr+=self.REAGENT_TITER.strip() if isinstance(self.REAGENT_TITER,str) else str(self.REAGENT_TITER).strip()
        tempStr+=','
        tempStr+=self.REAGENT_AC50_UNIT.strip() if isinstance(self.REAGENT_AC50_UNIT,str) else str(self.REAGENT_AC50_UNIT).strip()
        tempStr+=','
        tempStr+=self.REAGENT_CAS.strip() if isinstance(self.REAGENT_CAS,str) else str(self.REAGENT_CAS).strip()
        tempStr+=','
        tempStr+=self.REAGENT_SMILES.strip() if isinstance(self.REAGENT_SMILES,str) else str(self.REAGENT_SMILES).strip()
        tempStr+=','
        tempStr+=self.REAGENT_LINK.strip() if isinstance(self.REAGENT_LINK,str) else str(self.REAGENT_LINK).strip()
        tempStr+=','
        tempStr+=self.REAGENT_ASSAYS.strip() if isinstance(self.REAGENT_ASSAYS,str) else str(self.REAGENT_ASSAYS).strip()
        tempStr+=','
        tempStr+=self.REAGENT_CONCENTRATION.strip() if isinstance(self.REAGENT_CONCENTRATION,str) else str(self.REAGENT_CONCENTRATION).strip()
        tempStr+=','
        tempStr+=self.REAGENT_MOLECULAR_WEIGHT.strip() if isinstance(self.REAGENT_MOLECULAR_WEIGHT,str) else str(self.REAGENT_MOLECULAR_WEIGHT).strip()
        tempStr+=','
        tempStr+=self.REAGENT_SHOW_HIDE.strip() if isinstance(self.REAGENT_SHOW_HIDE,str) else str(self.REAGENT_SHOW_HIDE).strip()
        tempStr+=','
        tempStr+=self.REAGENT_MOA.strip() if isinstance(self.REAGENT_MOA,str) else str(self.REAGENT_MOA).strip()
        tempStr+='\n' 
        return tempStr 

    def toTSV(self):
        tempStr=''
        tempStr+=self.ID.strip() if isinstance(self.ID,str) else str(self.ID).strip()
        tempStr+='\t'
        tempStr+=self.SAMPLE_ID.strip() if isinstance(self.SAMPLE_ID,str) else str(self.SAMPLE_ID).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_NAME.strip() if isinstance(self.REAGENT_NAME,str) else str(self.REAGENT_NAME).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_COMMON_NAME.strip() if isinstance(self.REAGENT_COMMON_NAME,str) else str(self.REAGENT_COMMON_NAME).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_CLASS.strip() if isinstance(self.REAGENT_CLASS,str) else str(self.REAGENT_CLASS).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_SOURCE.strip() if isinstance(self.REAGENT_SOURCE,str) else str(self.REAGENT_SOURCE).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_LOT.strip() if isinstance(self.REAGENT_LOT,str) else str(self.REAGENT_LOT).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_TITER.strip() if isinstance(self.REAGENT_TITER,str) else str(self.REAGENT_TITER).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_AC50_UNIT.strip() if isinstance(self.REAGENT_AC50_UNIT,str) else str(self.REAGENT_AC50_UNIT).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_CAS.strip() if isinstance(self.REAGENT_CAS,str) else str(self.REAGENT_CAS).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_SMILES.strip() if isinstance(self.REAGENT_SMILES,str) else str(self.REAGENT_SMILES).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_LINK.strip() if isinstance(self.REAGENT_LINK,str) else str(self.REAGENT_LINK).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_ASSAYS.strip() if isinstance(self.REAGENT_ASSAYS,str) else str(self.REAGENT_ASSAYS).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_CONCENTRATION.strip() if isinstance(self.REAGENT_CONCENTRATION,str) else str(self.REAGENT_CONCENTRATION).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_MOLECULAR_WEIGHT.strip() if isinstance(self.REAGENT_MOLECULAR_WEIGHT,str) else str(self.REAGENT_MOLECULAR_WEIGHT).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_SHOW_HIDE.strip() if isinstance(self.REAGENT_SHOW_HIDE,str) else str(self.REAGENT_SHOW_HIDE).strip()
        tempStr+='\t'
        tempStr+=self.REAGENT_MOA.strip() if isinstance(self.REAGENT_MOA,str) else str(self.REAGENT_MOA).strip()
        tempStr+='\n' 
        return tempStr 

    def toTuple(self):
        return (self.ID,self.SAMPLE_ID,self.REAGENT_NAME,self.REAGENT_COMMON_NAME,self.REAGENT_CLASS,self.REAGENT_SOURCE,self.REAGENT_LOT,self.REAGENT_TITER,self.REAGENT_AC50_UNIT,self.REAGENT_CAS,self.REAGENT_SMILES,self.REAGENT_LINK,self.REAGENT_ASSAYS,self.REAGENT_CONCENTRATION,self.REAGENT_MOLECULAR_WEIGHT,self.REAGENT_SHOW_HIDE,self.REAGENT_MOA)
    @classmethod
    def fromTuple(cls,myTuple):
        return cls(myTuple['ID'],myTuple['SAMPLE_ID'],myTuple['REAGENT_NAME'],myTuple['REAGENT_COMMON_NAME'],myTuple['REAGENT_CLASS'],myTuple['REAGENT_SOURCE'],myTuple['REAGENT_LOT'],myTuple['REAGENT_TITER'],myTuple['REAGENT_AC50_UNIT'],myTuple['REAGENT_CAS'],myTuple['REAGENT_SMILES'],myTuple['REAGENT_LINK'],myTuple['REAGENT_ASSAYS'],myTuple['REAGENT_CONCENTRATION'],myTuple['REAGENT_MOLECULAR_WEIGHT'],myTuple['REAGENT_SHOW_HIDE'],myTuple['REAGENT_MOA'])

    @classmethod
    def getHeaderCSV(cls):
        return 'ID'+','+'SAMPLE_ID'+','+'REAGENT_NAME'+','+'REAGENT_COMMON_NAME'+','+'REAGENT_CLASS'+','+'REAGENT_SOURCE'+','+'REAGENT_LOT'+','+'REAGENT_TITER'+','+'REAGENT_AC50_UNIT'+','+'REAGENT_CAS'+','+'REAGENT_SMILES'+','+'REAGENT_LINK'+','+'REAGENT_ASSAYS'+','+'REAGENT_CONCENTRATION'+','+'REAGENT_MOLECULAR_WEIGHT'+','+'REAGENT_SHOW_HIDE'+','+'REAGENT_MOA'+','+'database_name'+','+'group_name'+','+'eb_group_number'+'\n'

    @classmethod
    def getHeaderTSV(cls):
        return 'ID'+'\t'+'SAMPLE_ID'+'\t'+'REAGENT_NAME'+'\t'+'REAGENT_COMMON_NAME'+'\t'+'REAGENT_CLASS'+'\t'+'REAGENT_SOURCE'+'\t'+'REAGENT_LOT'+'\t'+'REAGENT_TITER'+'\t'+'REAGENT_AC50_UNIT'+'\t'+'REAGENT_CAS'+'\t'+'REAGENT_SMILES'+'\t'+'REAGENT_LINK'+'\t'+'REAGENT_ASSAYS'+'\t'+'REAGENT_CONCENTRATION'+'\t'+'REAGENT_MOLECULAR_WEIGHT'+'\t'+'REAGENT_SHOW_HIDE'+'\t'+'REAGENT_MOA'+'\t'+'database_name'+'\t'+'group_name'+'\t'+'eb_group_number'+'\n'

