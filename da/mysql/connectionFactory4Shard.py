#import mysql.connector
#from mysql.connector import Error

import MySQLdb
#from   MySQLdb.connect import Error
import configparser
import os

class connectionFactory4Shard:
    def __init__(self, host,db,user,passwd):
        self.host=host
        self.db=db
        self.user=user
        self.passwd=passwd

    def __getConnection(self):

        connection = None

        try:
            connection = MySQLdb.connect(
			host   = self.host,
			user   = self.user,
			passwd = self.passwd,
			db     = self.db
		)
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
            return None
        ##print('---Connect to Group DB on '+self.host+' / '+self.db+' / '+self.user+ '  successful---')
        return connection
    @classmethod
    def getConnection(cls,myHost,myUser,myPassword,myDB=''):

        connection = None
        if not myDB:
            try:
                connection = MySQLdb.connect(
			host   = myHost,
			user   = myUser,
			passwd = myPassword
			
		)
            except (MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)
                print(' in CF4Shard')
                return None

        else:
            try:
                connection = MySQLdb.connect(
			host   = myHost,
			user   = myUser,
			passwd = myPassword,
                        db=myDB
			
		)
            except (MySQLdb.Error, MySQLdb.Warning) as e:
                print(e)
                print(' in CF4Shard')
                return None
        #print('---Connect to DB on '+myHost+' with user  '+myUser+ '  successful---')
        return connection

    
    # C/U/D and other DDL ,no R
    @classmethod
    def runSQL(cls,myHost,myDB,myUser,myPassword,mySQL):
        connection=None
        connection=cls.getConnection(myHost,myDB,myUser,myPassword)
        #cursor = connection.cursor()
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            cursor.execute(mySQL)
            connection.commit()
            connection.close()
            #print("---Run C/U/D Query successful on Shard CF---")
            return myHost+" "+myDB+" run SQL sucessfully"
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
            return 'FAIL in '+ myHost+" "+myDB+", reason:"+e
            #return None

    @classmethod
    def runSQLWithExternalConnection(cls,myConnection,mySQL):
        #cursor = connection.cursor()
        cursor = myConnection.cursor(MySQLdb.cursors.DictCursor)

        try:
            cursor.execute(mySQL)
            #myConnection.commit()
            cursor.close()

            #print("---Run C/U/D Query successful on Shard CF---")
            return "Sucessfully"
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
            return 'Fail, reason: '+str(e)
            #return None
    
    # R :
    @classmethod
    def runSelect(cls,myHost,myUser,myPassword,mySQL,myDB=''):
        connection=None
        connection=cls.getConnection(myHost,myUser,myPassword,myDB)
        ##cursor = connection.cursor()
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)

        result = None
        try:
            cursor.execute(mySQL)
            result = cursor.fetchall()
            connection.close()
            return result
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
            return None


    @classmethod
    def getReportCSVColumnHeader(cls,myHost,myUser,myPassword,mySQL,myDB=''):
        connection=None
        connection=cls.getConnection(myHost,myUser,myPassword,myDB)
        ##cursor = connection.cursor()
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)

        result = None
        try:
            cursor.execute(mySQL)
            result = cursor.fetchall()
            ##-------
            tempStr=''
            if cursor.description:
                for i in cursor.description:
                    tempStr=tempStr+','+i[0]
                tempStr=tempStr.lstrip(',')
            ##print(tempStr)
      
            ##-------
            connection.close()
            return tempStr
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
            return None

    #sql = '''
    #INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
    #VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    #'''
    
    #val = [
    #(7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'), 
    #(8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
    #]


    def runInsertListOfTuple(self,sql, val):
        connection=None
        connection=self.__getConnection()
        ##cursor = connection.cursor()
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.executemany(sql, val)
            connection.commit()
            connection.close()
            print("Query successful")
        except Error as err:
            print("Error: '{err}'")
    


