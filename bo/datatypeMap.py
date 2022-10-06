##File          : report.py 
##Date Created  :03/18/2022, 16:08:46
##Author        : Ken Liu 

#From ODP Oracle Db , run below SQL to get how many data type in your curret DB,To do short cut , only focus these datatype

#SELECT distinct DATA_TYPE FROM COLS order by 1 ;

#BLOB
#CLOB
#DATE
#FLOAT
#NUMBER
#NVARCHAR2
#TIMESTAMP(6)
#VARCHAR2



class datatypeMap:
    def __init__(self):
        pass

    myBO={}
    #https://livesql.oracle.com/apex/livesql/file/tutorial_FIMJZ2NPQ4AWTCE0B329BW3GX.html

    #1: Oracle Character Data Types: 
    #varchar2
    #char
    #clob
    myBO['VARCHAR2'] = 'varchar'
    myBO['CHAR']='char'
    myBO['CLOB'] ='text'

    myBO['NCHAR']= 'char'
    myBO['VARCHAR'] ='varchar'
    myBO['NVARCHAR'] ='varchar'
    
    myBO['NVARCHAR2'] ='varchar'
    myBO['STRING'] ='varchar'


    #2: Oarcel Numeric Data Types
    #number
    #float
    #binary_float
    #binary_double

    myBO['NUMBER'] = 'numeric'
    myBO['FLOAT']='double precision'
    myBO['BINARY_FLOAT']='numeric'
    myBO['BINARY_DOUBLE']='numeric'

    #3: Oracle Datetime and Interval Data Types

    #date
    #timestamp
    #timestamp with time zone
    #timestamp with local time zone
    myBO['DATE']='timestamp'
    myBO['TIMESTAMP']='timestamp'
    myBO['TIMESTAMP WITH TIME ZONE']='timestamp with time zone' 
    myBO['TIMESTAMP WITH LOCAL TIME ZONE']='timestamp with time zone'
 
    #4; Oracle Binary Data Types
    #RAW
    #BLOB
    myBO['RAW']='bytea'
    myBO['BLOB']='bytea'

    myBO['LONG'] ='text'
    myBO['LONG RAW']= 'bytea'
   
    myBO['NCLOB']='text'
    myBO['BFILE']='bytea'
    myBO['RAW(16)']='uuid'
    myBO['RAW(32)']='uuid'
    myBO['ROWID']='oid'
    myBO['UROWID']='oid'
    
    myBO['DEC']='decimal'
    myBO['DECIMAL']='decimal'
    myBO['DOUBLE PRECISION']='double precision'
    myBO['INT']='integer'
    myBO['INTEGER']='integer'
    myBO['BINARY_INTEGER']='integer'
    myBO['PLS_INTEGER']='integer'
    myBO['SMALLINT']='smallint'
    myBO['REAL']='real'
    
    myBO['BOOLEAN']='boolean'
    myBO['INTERVAL']='interval'
    myBO['XMLTYPE']='xml'
    myBO['TIMESTAMP(6)']='timestamp'
    myBO['SDO_GEOMETRY']='geometry'
    
    def __str__(self):
        return 'This class hold the Oracle dataType to PostgreSQL dataType myBOping'

    @classmethod
    def toCSV(cls):
        tempStr=''
        for key in myBO:
            tempStr+=key+':'+myBO[key]+','
        
        tempStr+='\n' 
        return tempStr 
    @classmethod
    def toTSV(cls):
        tempStr=''
        for key in myBO:
            tempStr+=key+':'+myBO[key]+'\t'

        tempStr+='\n' 
        return tempStr 
    @classmethod
    def mapDatatype(cls,sourceDT):
        #targetDT=''
        for key in cls.myBO:
            if key==sourceDT.strip().upper(): #<---All key should be keep upcase in this class
                return cls.myBO[key]
        return None

