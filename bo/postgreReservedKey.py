##File          : report.py 
##Date Created  :03/18/2022, 16:08:46
##Author        : Ken Liu 

#You can get PostgreSQL reserved words as below:

#postgres=# select concat(E'myBO[\'',upper(word),E'\']=',E'\'',catdesc,E'\'' ) from pg_get_keywords() where catcode='R' order by word;
#                concat               
#--------------------------------------
#myBO['ALL']='reserved'
#myBO['ANALYSE']='reserved'
#myBO['ANALYZE']='reserved'
#myBO['AND']='reserved'


class postgreReservedKey:
    def __init__(self):
        pass

    myBO={}
    myBO['ALL']='reserved'
    myBO['ANALYSE']='reserved'
    myBO['ANALYZE']='reserved'
    myBO['AND']='reserved'
    myBO['ANY']='reserved'
    myBO['ARRAY']='reserved'
    myBO['AS']='reserved'
    myBO['ASC']='reserved'
    myBO['ASYMMETRIC']='reserved'
    myBO['BOTH']='reserved'
    myBO['CASE']='reserved'
    myBO['CAST']='reserved'
    myBO['CHECK']='reserved'
    myBO['COLLATE']='reserved'
    myBO['COLUMN']='reserved'
    myBO['CONSTRAINT']='reserved'
    myBO['CREATE']='reserved'
    myBO['CURRENT_CATALOG']='reserved'
    myBO['CURRENT_DATE']='reserved'
    myBO['CURRENT_ROLE']='reserved'
    myBO['CURRENT_TIME']='reserved'
    myBO['CURRENT_TIMESTAMP']='reserved'
    myBO['CURRENT_USER']='reserved'
    myBO['DEFAULT']='reserved'
    myBO['DEFERRABLE']='reserved'
    myBO['DESC']='reserved'
    myBO['DISTINCT']='reserved'
    myBO['DO']='reserved'
    myBO['ELSE']='reserved'
    myBO['END']='reserved'
    myBO['EXCEPT']='reserved'
    myBO['FALSE']='reserved'
    myBO['FETCH']='reserved'
    myBO['FOR']='reserved'
    myBO['FOREIGN']='reserved'
    myBO['FROM']='reserved'
    myBO['GRANT']='reserved'
    myBO['GROUP']='reserved'
    myBO['HAVING']='reserved'
    myBO['IN']='reserved'
    myBO['INITIALLY']='reserved'
    myBO['INTERSECT']='reserved'
    myBO['INTO']='reserved'
    myBO['LATERAL']='reserved'
    myBO['LEADING']='reserved'
    myBO['LIMIT']='reserved'
    myBO['LOCALTIME']='reserved'
    myBO['LOCALTIMESTAMP']='reserved'
    myBO['NOT']='reserved'
    myBO['NULL']='reserved'
    myBO['OFFSET']='reserved'
    myBO['ON']='reserved'
    myBO['ONLY']='reserved'
    myBO['OR']='reserved'
    myBO['ORDER']='reserved'
    myBO['PLACING']='reserved'
    myBO['PRIMARY']='reserved'
    myBO['REFERENCES']='reserved'
    myBO['RETURNING']='reserved'
    myBO['SELECT']='reserved'
    myBO['SESSION_USER']='reserved'
    myBO['SOME']='reserved'
    myBO['SYMMETRIC']='reserved'
    myBO['TABLE']='reserved'
    myBO['THEN']='reserved'
    myBO['TO']='reserved'
    myBO['TRAILING']='reserved'
    myBO['TRUE']='reserved'
    myBO['UNION']='reserved'
    myBO['UNIQUE']='reserved'
    myBO['USER']='reserved'
    myBO['USING']='reserved'
    myBO['VARIADIC']='reserved'
    myBO['WHEN']='reserved'
    myBO['WHERE']='reserved'
    myBO['WINDOW']='reserved'
    myBO['WITH']='reserved'   

    def __str__(self):
        return 'This class hold All PostgreSQL reserved words which we need to avoid them when create table or column name,even function name'

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
    def reserved(cls,myStr):
        #targetDT=''
        for key in cls.myBO:
            if key==myStr.strip().upper(): #<---All key should be keep upcase in this class
                return True
        #print('      --checked and not reserved word: '+myStr)
        return False

