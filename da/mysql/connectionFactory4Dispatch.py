
import MySQLdb
#from   MySQLdb.connect import Error
from    MySQLdb         import Error
import configparser
import os

class connectionFactory4Dispatch :
    @classmethod
    #def getConnection(host_name, user_name, user_password):
    def __getConnection(cls):
        # Get user/password from protected my.cnf file
        configParser = configparser.RawConfigParser()
        configParser.read('%s/.my.cnf' % os.path.expanduser('~'))
        try:
           myUser = configParser.get('client', 'user')
           myPassword = configParser.get('client', 'password')
           ##print('Got you credentail as below:'+myUser+" "+myPassword)
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError) as e:
           print('FAILED: Reading ini file for username/password - Reason: %s' % e)
        

        myHost   = 'dispatch-slave-vip.mp.prd.chi1'   #<--PROD
        #myHost   = 'ddb101.mp.pre.chi1'               #<--PRE_PROD
        #myHost   = 'ddb101.mp.qa.clt4'                #<--QA
        #myHost   = 'ddb101.mp.tst.clt4'               #<--TST
        #myHost   = 'ddb101.mp.dev.clt4'               #<--DEV
        #myHost   = 'ddb101.mp.sbx5.clt4'              #<--SANDBOX 5
        
        myDB='dispatch'

        connection = None

        try:
            connection = MySQLdb.connect(
			host   = myHost,
			user   = myUser,
			passwd = myPassword,
			db     = myDB
		)
        except Error as err:
            print("Error: '{err}'")
        if connection is None:
           print("---Connect to dispatch DB  FAIL---")
        return connection

    @classmethod
    # C/U/D and other DDL ,no R
    def runSQL(cls, query):
        connection=None
        connection=cls.__getConnection()
        #cursor = connection.cursor()
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)

        try:
            cursor.execute(query)
            connection.commit()
            connection.close()
            #print("---Run C/U/D Query successful---")
        except Error as err:
            print("Error: '{err}'")

    @classmethod
    # R :
    def runSelect(cls, query):
        connection=None
        connection=cls.__getConnection()
        ##cursor = connection.cursor()
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)

        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            connection.close()
            return result
        except Error as err:
            print("Error: '{err}'")     


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
        cursor = connection.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.executemany(sql, val)
            connection.commit()
            connection.close()
            print("Query successful")
        except Error as err:
            print("Error: '{err}'")
    


