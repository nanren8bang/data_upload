
import cx_Oracle
#import cx_Oracle.Error as Error

import configparser
import os

class connectionFactory:
    @classmethod
    #def getConnection(host_name, user_name, user_password):
    def __getConnection(cls):
        # Get user/password from protected my.cnf file
        configParser = configparser.RawConfigParser()
        configParser.read('%s/.my.cnf' % os.path.expanduser('~'))
        try:

           myUser        = configParser.get('oracle', 'user')
           myPassword    = configParser.get('oracle', 'password')
           myHost        = configParser.get('oracle', 'host')
           myPort        = configParser.get('oracle', 'port')
           myServiceName = configParser.get('oracle', 'servicename')
       

        except (configparser.NoSectionError, configparser.NoOptionError) as e:
           print('FAILED: Reading ini file for username/password - Reason: %s' % e)

        myDSN = cx_Oracle.makedsn(myHost, myPort, myServiceName) #see  https://datatofish.com/how-to-connect-python-to-an-oracle-database-using-cx_oracle/

        connection = None
        #https://www.oracletutorial.com/python-oracle/connecting-to-oracle-database-in-python/
        try: 
            connection = cx_Oracle.connect(
			 user=myUser,
			 password=myPassword,
			 dsn=myDSN
                         #encoding="UTF-8"
		)
        except cx_Oracle.Error as err:
            print(err)
        finally:
            #if connection:
            #    connection.close()
            pass
        #print("---Connect to cx_Oracle successfully---")
        return connection

    # C/U/D and other DDL ,no R
    @classmethod
    def runSQL(cls, query):
        connection=None
        connection=cls.__getConnection()
        #cursor = connection.cursor()
        cursor = connection.cursor(cx_Oracle.cursors.DictCursor)

        try:
            cursor.execute(query)
            connection.commit()
            connection.close()
            print("---Run C/U/D Query successful---")
        except Error as err:
            print(err)

    # R :
    @classmethod
    def runSelect1(cls, query):
        #connection=None
        connection=cls.__getConnection()
        cursor = connection.cursor()
        #cursor = connection.cursor(cx_Oracle.cursor.DictCursor)

        result = None
        try:
            cursor.prefetchrows = 1000
            cursor.arraysize = 1000   #<--default is 100 , see:https://cx-oracle.readthedocs.io/en/latest/user_guide/tuning.html?highlight=arraysize#choosing-values-for-arraysize-and-prefetchrows
            cursor.execute(query)
            #<--SELECT fieldA, fieldB FROM table ORDER BY fieldA  OFFSET 5 ROWS FETCH NEXT 14 ROWS ONLY
 
            columnNames = [d[0] for d in cursor.description]
            myList=[]
            for cur in cursor:
                #print(type(row)) # type(row)=tuple
                #if row:
                row=list(cur)  ##<--convert tuple into list to make it mutable (tuple is immutable)
                j=0
                for i in cursor.description:
                    if str(i[1]).split(' ')[1][:-1]=='DB_TYPE_CLOB' or str(i[1]).split(' ')[1][:-1]=='DB_TYPE_BLOB':
                        print('data_type='+str(i[1]).split(' ')[1][:-1])
                        if row[j]:
                            row[j]=row[j].read() #<---read CLOB/BLOB and save it into list
                            #print('From query='+query)
                            #print(row[j])        #<---for test                            
                        else: #<--avoid err 'null object withour attribute read'
                            row[j]=''
                        #del row[j]
                    j=j+1

                myList.append(dict(zip(columnNames,row)))

            #result = [dict((cursor.description[i][0], value) \
            #   for i, value in enumerate(row)) for row in cursor.fetchall()]
            #results = cursor.fetchall()
            #for result in results:
                #myTumple=dict(zip(columnNames,result))
                #myList.append(myTumple)
                #myList.append(dict(zip(columnNames,result)))

            return myList
        except cx_Oracle.Error as err:
            print(err)     
        finally:
            connection.close()

    @classmethod
    def runSelect(cls, query):
        #connection=None
        connection=cls.__getConnection()
        cursor = connection.cursor()
        #cursor = connection.cursor(cx_Oracle.cursor.DictCursor)

        result = None
        try:
            cursor.execute(query)
            result = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            #for above line , see here: https://github.com/oracle/python-cx_Oracle/issues/410
            #result = cursor.fetchall()
            #columnNames = [d[0] for d in cursor.description]
            #columnNames = [d[0] for d in cursor.description]
            #print(columnNames)
            #connection.close()
            return result
        except cx_Oracle.Error as err:
            print(err)     
        finally:
            connection.close()


    @classmethod
    #sql = '''
    #INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
    #VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    #'''
    
    #val = [
    #(7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'), 
    #(8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
    #]


    def runInsertListOfTuple(cls,sql, val):
        connection=None
        connection=cls.__getConnection()
        ##cursor = connection.cursor()
        cursor = connection.cursor(cx_Oracle.cursors.DictCursor)
        try:
            cursor.executemany(sql, val)
            connection.commit()
            connection.close()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
    


