

import mysql.connector
from mysql.connector import Error

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
           myUser = configParser.get('mysqlD', 'user')
           myPassword = configParser.get('mysqlD', 'password')
           myHost = configParser.get('mysqlD', 'host')
           myDatabase = configParser.get('mysqlD', 'database')
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError) as e:
           print('FAILED: Reading ini file for username/password - Reason: %s' % e)

        connection = None

        try:
            connection=mysql.connector.connect(
			host   = myHost,
			user   = myUser,
			password = myPassword,
			database = myDatabase
		)
            #if connection.is_connected():
                #db_Info = connection.get_server_info()
                #print("Sucessfully connected to MySQL Server version ", db_Info)
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            pass
            #if connection.is_connected():
            #    cursor.close()
            #    connection.close()
            #    print("MySQL connection is closed")

        return connection

    @classmethod
    # C/U/D and other DDL ,no R
    def runSQL(cls, query):
        connection=None
        connection=cls.__getConnection()
        #cursor = connection.cursor()
        cursor = connection.cursor(dictionary=True)
        #print('In runSQL, sql='+query)
        try:
            ##cursor.execute(query,multi=True)
            cursor.execute(query)
            connection.commit()
            #connection.close()
            #print("---Run C/U/D Query successful---")
        except Error as e:
            print("Error:",e)
        finally:
            connection.close()

    @classmethod
    # R :
    def runSelect(cls, query):
        connection=None
        connection=cls.__getConnection()
        ##cursor = connection.cursor()
        cursor = connection.cursor(dictionary=True)

        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            #connection.close()
            return result
        except Error as e:
            print("Error:",e)     
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
        cursor = connection.cursor(dictionary=True)
        #print("\n In runInsertListOfTuple class method ")
        #print("\nsql=%s\n"%(sql))
        #print("\nval=%s\n"%(val))
        try:
            cursor.executemany(sql, val)
            connection.commit()
            #connection.close()
            #print("Insert ListOfTuple successful")
        except Error as e:
            print("Error from runInsertListOfTuple:",e)   
        finally:
            connection.close()


