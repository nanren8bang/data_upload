##File          : column.py 
##Date Created  : 05/05/2022, 19:48:22
##Author        : Ken Liu 

from typing     import List, Optional,Any  
from pydantic   import BaseModel,ValidationError,validator   

class column(BaseModel):
    TABLE_SCHEMA: Any
    TABLE_NAME: Any
    COLUMN_NAME: Any
    ORDINAL_POSITION: Any
    COLUMN_DEFAULT: Any
    IS_NULLABLE: Any
    DATA_TYPE: Any
    CHARACTER_MAXIMUM_LENGTH: Any
    CHARACTER_OCTET_LENGTH: Any
    NUMERIC_PRECISION: Any
    NUMERIC_SCALE: Any
    DATETIME_PRECISION: Any
    CHARACTER_SET_NAME: Any
    COLLATION_NAME: Any
    COLUMN_TYPE: Any
    COLUMN_KEY: Any
    EXTRA: Any
    PRIVILEGES: Any
    COLUMN_COMMENT: Any
    IS_GENERATED: Any
    GENERATION_EXPRESSION: Any

    def __init__(self,TABLE_SCHEMA ,TABLE_NAME,COLUMN_NAME,ORDINAL_POSITION,COLUMN_DEFAULT,IS_NULLABLE,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH,CHARACTER_OCTET_LENGTH,NUMERIC_PRECISION,NUMERIC_SCALE,DATETIME_PRECISION,CHARACTER_SET_NAME,COLLATION_NAME,COLUMN_TYPE,COLUMN_KEY,EXTRA,PRIVILEGES,COLUMN_COMMENT,IS_GENERATED,GENERATION_EXPRESSION ):
        super().__init__(TABLE_SCHEMA =TABLE_SCHEMA ,TABLE_NAME=TABLE_NAME,COLUMN_NAME=COLUMN_NAME,ORDINAL_POSITION=ORDINAL_POSITION,COLUMN_DEFAULT=COLUMN_DEFAULT,IS_NULLABLE=IS_NULLABLE,DATA_TYPE=DATA_TYPE,CHARACTER_MAXIMUM_LENGTH=CHARACTER_MAXIMUM_LENGTH,CHARACTER_OCTET_LENGTH=CHARACTER_OCTET_LENGTH,NUMERIC_PRECISION=NUMERIC_PRECISION,NUMERIC_SCALE=NUMERIC_SCALE,DATETIME_PRECISION=DATETIME_PRECISION,CHARACTER_SET_NAME=CHARACTER_SET_NAME,COLLATION_NAME=COLLATION_NAME,COLUMN_TYPE=COLUMN_TYPE,COLUMN_KEY=COLUMN_KEY,EXTRA=EXTRA,PRIVILEGES=PRIVILEGES,COLUMN_COMMENT=COLUMN_COMMENT,IS_GENERATED=IS_GENERATED,GENERATION_EXPRESSION=GENERATION_EXPRESSION)

    def __str__(self):
        return 'This class hold report detail values:TABLE_SCHEMA ,TABLE_NAME,COLUMN_NAME,ORDINAL_POSITION,COLUMN_DEFAULT,IS_NULLABLE,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH,CHARACTER_OCTET_LENGTH,NUMERIC_PRECISION,NUMERIC_SCALE,DATETIME_PRECISION,CHARACTER_SET_NAME,COLLATION_NAME,COLUMN_TYPE,COLUMN_KEY,EXTRA,PRIVILEGES,COLUMN_COMMENT,IS_GENERATED,GENERATION_EXPRESSION'

    def toCSV(self):
        tempStr=''
        tempStr+=self.TABLE_SCHEMA .strip() if isinstance(self.TABLE_SCHEMA ,str) else str(self.TABLE_SCHEMA ).strip()
        tempStr+=','
        tempStr+=self.TABLE_NAME.strip() if isinstance(self.TABLE_NAME,str) else str(self.TABLE_NAME).strip()
        tempStr+=','
        tempStr+=self.COLUMN_NAME.strip() if isinstance(self.COLUMN_NAME,str) else str(self.COLUMN_NAME).strip()
        tempStr+=','
        tempStr+=self.ORDINAL_POSITION.strip() if isinstance(self.ORDINAL_POSITION,str) else str(self.ORDINAL_POSITION).strip()
        tempStr+=','
        tempStr+=self.COLUMN_DEFAULT.strip() if isinstance(self.COLUMN_DEFAULT,str) else str(self.COLUMN_DEFAULT).strip()
        tempStr+=','
        tempStr+=self.IS_NULLABLE.strip() if isinstance(self.IS_NULLABLE,str) else str(self.IS_NULLABLE).strip()
        tempStr+=','
        tempStr+=self.DATA_TYPE.strip() if isinstance(self.DATA_TYPE,str) else str(self.DATA_TYPE).strip()
        tempStr+=','
        tempStr+=self.CHARACTER_MAXIMUM_LENGTH.strip() if isinstance(self.CHARACTER_MAXIMUM_LENGTH,str) else str(self.CHARACTER_MAXIMUM_LENGTH).strip()
        tempStr+=','
        tempStr+=self.CHARACTER_OCTET_LENGTH.strip() if isinstance(self.CHARACTER_OCTET_LENGTH,str) else str(self.CHARACTER_OCTET_LENGTH).strip()
        tempStr+=','
        tempStr+=self.NUMERIC_PRECISION.strip() if isinstance(self.NUMERIC_PRECISION,str) else str(self.NUMERIC_PRECISION).strip()
        tempStr+=','
        tempStr+=self.NUMERIC_SCALE.strip() if isinstance(self.NUMERIC_SCALE,str) else str(self.NUMERIC_SCALE).strip()
        tempStr+=','
        tempStr+=self.DATETIME_PRECISION.strip() if isinstance(self.DATETIME_PRECISION,str) else str(self.DATETIME_PRECISION).strip()
        tempStr+=','
        tempStr+=self.CHARACTER_SET_NAME.strip() if isinstance(self.CHARACTER_SET_NAME,str) else str(self.CHARACTER_SET_NAME).strip()
        tempStr+=','
        tempStr+=self.COLLATION_NAME.strip() if isinstance(self.COLLATION_NAME,str) else str(self.COLLATION_NAME).strip()
        tempStr+=','
        tempStr+=self.COLUMN_TYPE.strip() if isinstance(self.COLUMN_TYPE,str) else str(self.COLUMN_TYPE).strip()
        tempStr+=','
        tempStr+=self.COLUMN_KEY.strip() if isinstance(self.COLUMN_KEY,str) else str(self.COLUMN_KEY).strip()
        tempStr+=','
        tempStr+=self.EXTRA.strip() if isinstance(self.EXTRA,str) else str(self.EXTRA).strip()
        tempStr+=','
        tempStr+=self.PRIVILEGES.strip() if isinstance(self.PRIVILEGES,str) else str(self.PRIVILEGES).strip()
        tempStr+=','
        tempStr+=self.COLUMN_COMMENT.strip() if isinstance(self.COLUMN_COMMENT,str) else str(self.COLUMN_COMMENT).strip()
        tempStr+=','
        tempStr+=self.IS_GENERATED.strip() if isinstance(self.IS_GENERATED,str) else str(self.IS_GENERATED).strip()
        tempStr+=','
        tempStr+=self.GENERATION_EXPRESSION.strip() if isinstance(self.GENERATION_EXPRESSION,str) else str(self.GENERATION_EXPRESSION).strip()
        tempStr+='\n' 
        return tempStr 

    def toTSV(self):
        tempStr=''
        tempStr+=self.TABLE_SCHEMA .strip() if isinstance(self.TABLE_SCHEMA ,str) else str(self.TABLE_SCHEMA ).strip()
        tempStr+='\t'
        tempStr+=self.TABLE_NAME.strip() if isinstance(self.TABLE_NAME,str) else str(self.TABLE_NAME).strip()
        tempStr+='\t'
        tempStr+=self.COLUMN_NAME.strip() if isinstance(self.COLUMN_NAME,str) else str(self.COLUMN_NAME).strip()
        tempStr+='\t'
        tempStr+=self.ORDINAL_POSITION.strip() if isinstance(self.ORDINAL_POSITION,str) else str(self.ORDINAL_POSITION).strip()
        tempStr+='\t'
        tempStr+=self.COLUMN_DEFAULT.strip() if isinstance(self.COLUMN_DEFAULT,str) else str(self.COLUMN_DEFAULT).strip()
        tempStr+='\t'
        tempStr+=self.IS_NULLABLE.strip() if isinstance(self.IS_NULLABLE,str) else str(self.IS_NULLABLE).strip()
        tempStr+='\t'
        tempStr+=self.DATA_TYPE.strip() if isinstance(self.DATA_TYPE,str) else str(self.DATA_TYPE).strip()
        tempStr+='\t'
        tempStr+=self.CHARACTER_MAXIMUM_LENGTH.strip() if isinstance(self.CHARACTER_MAXIMUM_LENGTH,str) else str(self.CHARACTER_MAXIMUM_LENGTH).strip()
        tempStr+='\t'
        tempStr+=self.CHARACTER_OCTET_LENGTH.strip() if isinstance(self.CHARACTER_OCTET_LENGTH,str) else str(self.CHARACTER_OCTET_LENGTH).strip()
        tempStr+='\t'
        tempStr+=self.NUMERIC_PRECISION.strip() if isinstance(self.NUMERIC_PRECISION,str) else str(self.NUMERIC_PRECISION).strip()
        tempStr+='\t'
        tempStr+=self.NUMERIC_SCALE.strip() if isinstance(self.NUMERIC_SCALE,str) else str(self.NUMERIC_SCALE).strip()
        tempStr+='\t'
        tempStr+=self.DATETIME_PRECISION.strip() if isinstance(self.DATETIME_PRECISION,str) else str(self.DATETIME_PRECISION).strip()
        tempStr+='\t'
        tempStr+=self.CHARACTER_SET_NAME.strip() if isinstance(self.CHARACTER_SET_NAME,str) else str(self.CHARACTER_SET_NAME).strip()
        tempStr+='\t'
        tempStr+=self.COLLATION_NAME.strip() if isinstance(self.COLLATION_NAME,str) else str(self.COLLATION_NAME).strip()
        tempStr+='\t'
        tempStr+=self.COLUMN_TYPE.strip() if isinstance(self.COLUMN_TYPE,str) else str(self.COLUMN_TYPE).strip()
        tempStr+='\t'
        tempStr+=self.COLUMN_KEY.strip() if isinstance(self.COLUMN_KEY,str) else str(self.COLUMN_KEY).strip()
        tempStr+='\t'
        tempStr+=self.EXTRA.strip() if isinstance(self.EXTRA,str) else str(self.EXTRA).strip()
        tempStr+='\t'
        tempStr+=self.PRIVILEGES.strip() if isinstance(self.PRIVILEGES,str) else str(self.PRIVILEGES).strip()
        tempStr+='\t'
        tempStr+=self.COLUMN_COMMENT.strip() if isinstance(self.COLUMN_COMMENT,str) else str(self.COLUMN_COMMENT).strip()
        tempStr+='\t'
        tempStr+=self.IS_GENERATED.strip() if isinstance(self.IS_GENERATED,str) else str(self.IS_GENERATED).strip()
        tempStr+='\t'
        tempStr+=self.GENERATION_EXPRESSION.strip() if isinstance(self.GENERATION_EXPRESSION,str) else str(self.GENERATION_EXPRESSION).strip()
        tempStr+='\n' 
        return tempStr 

    def toTuple(self):
        return (self.TABLE_SCHEMA,self.TABLE_NAME,self.COLUMN_NAME,self.ORDINAL_POSITION,self.COLUMN_DEFAULT,self.IS_NULLABLE,self.DATA_TYPE,self.CHARACTER_MAXIMUM_LENGTH,self.CHARACTER_OCTET_LENGTH,self.NUMERIC_PRECISION,self.NUMERIC_SCALE,self.DATETIME_PRECISION,self.CHARACTER_SET_NAME,self.COLLATION_NAME,self.COLUMN_TYPE,self.COLUMN_KEY,self.EXTRA,self.PRIVILEGES,self.COLUMN_COMMENT,self.IS_GENERATED,self.GENERATION_EXPRESSION)
    @classmethod
    def fromDict(cls,myDict):
        return cls(myDict['TABLE_SCHEMA'],myDict['TABLE_NAME'],myDict['COLUMN_NAME'],myDict['ORDINAL_POSITION'],myDict['COLUMN_DEFAULT'],myDict['IS_NULLABLE'],myDict['DATA_TYPE'],myDict['CHARACTER_MAXIMUM_LENGTH'],myDict['CHARACTER_OCTET_LENGTH'],myDict['NUMERIC_PRECISION'],myDict['NUMERIC_SCALE'],myDict['DATETIME_PRECISION'],myDict['CHARACTER_SET_NAME'],myDict['COLLATION_NAME'],myDict['COLUMN_TYPE'],myDict['COLUMN_KEY'],myDict['EXTRA'],myDict['PRIVILEGES'],myDict['COLUMN_COMMENT'],myDict['IS_GENERATED'],myDict['GENERATION_EXPRESSION'])

    @classmethod
    def getHeaderCSV(cls):
        return 'TABLE_SCHEMA'+','+'TABLE_NAME'+','+'COLUMN_NAME'+','+'ORDINAL_POSITION'+','+'COLUMN_DEFAULT'+','+'IS_NULLABLE'+','+'DATA_TYPE'+','+'CHARACTER_MAXIMUM_LENGTH'+','+'CHARACTER_OCTET_LENGTH'+','+'NUMERIC_PRECISION'+','+'NUMERIC_SCALE'+','+'DATETIME_PRECISION'+','+'CHARACTER_SET_NAME'+','+'COLLATION_NAME'+','+'COLUMN_TYPE'+','+'COLUMN_KEY'+','+'EXTRA'+','+'PRIVILEGES'+','+'COLUMN_COMMENT'+','+'IS_GENERATED'+','+'GENERATION_EXPRESSION'+','+'database_name'+','+'group_name'+','+'eb_group_number'+'\n'

    @classmethod
    def getHeaderTSV(cls):
        return 'TABLE_SCHEMA'+'\t'+'TABLE_NAME'+'\t'+'COLUMN_NAME'+'\t'+'ORDINAL_POSITION'+'\t'+'COLUMN_DEFAULT'+'\t'+'IS_NULLABLE'+'\t'+'DATA_TYPE'+'\t'+'CHARACTER_MAXIMUM_LENGTH'+'\t'+'CHARACTER_OCTET_LENGTH'+'\t'+'NUMERIC_PRECISION'+'\t'+'NUMERIC_SCALE'+'\t'+'DATETIME_PRECISION'+'\t'+'CHARACTER_SET_NAME'+'\t'+'COLLATION_NAME'+'\t'+'COLUMN_TYPE'+'\t'+'COLUMN_KEY'+'\t'+'EXTRA'+'\t'+'PRIVILEGES'+'\t'+'COLUMN_COMMENT'+'\t'+'IS_GENERATED'+'\t'+'GENERATION_EXPRESSION'+'\t'+'database_name'+'\t'+'group_name'+'\t'+'eb_group_number'+'\n'

