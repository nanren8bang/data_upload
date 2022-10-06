##File          : variant_drugDA.py 
##Date Created  : 04/05/2022, 19:48:22
##Author        : Ken Liu 

 
from da.mysql.connectionFactory import connectionFactory as CF 


class variant_drugDA:
    
    @staticmethod
    def runSQL(mySQL):
        CF.runSQL(mySQL)
