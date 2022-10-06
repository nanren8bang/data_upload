

import mysql.connector
from mysql.connector import Error

import configparser
import os

class connectionFactory:
    @classmethod
     
    def __getConnection(cls):
         
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
             
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            pass
             

        return connection

    @classmethod
    
    def runSQL(cls, query):
        connection=None
        connection=cls.__getConnection()
        
        cursor = connection.cursor(dictionary=True)
         
        try:
            
            cursor.execute(query)
            connection.commit()
            
        except Error as e:
            print("Error:",e)
        finally:
            connection.close()

    @classmethod
    
    def runSelect(cls, query):
        connection=None
        connection=cls.__getConnection()
        ##cursor = connection.cursor()
        cursor = connection.cursor(dictionary=True)

        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
             
            return result
        except Error as e:
            print("Error:",e)     
        finally:
            connection.close()

     

    def runInsertListOfTuple(cls,sql, val):
        connection=None
        connection=cls.__getConnection()
        cursor = connection.cursor(dictionary=True)
         
        try:
            cursor.executemany(sql, val)
            connection.commit()
             
        except Error as e:
            print("Error from runInsertListOfTuple:",e)   
        finally:
            connection.close()


