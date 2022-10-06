##File          : variant_drugDA.py 
##Date Created  : 05/05/2022, 19:48:22
##Author        : Ken Liu 

from bo.mysql.variant_drug import variant_drug as BO 
from da.mysql.connectionFactory import connectionFactory as CF 


class variant_drugDA:
    ##1: C
    @staticmethod
    def runInsertListOfTuple(sql, val):
        CF.runInsertListOfTuple(sql, val)

    ##2: R


    @staticmethod
    def getAll():
        myBOList=[]
        mySQL="""
            select *  from variant_drug
        """
        results=CF.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.fromDict(result))
        return myBOList
        

    @staticmethod
    def getOne():
        pass
        

    ##3: U


    ##4: D


    ##5: Misc


    @staticmethod
    def runSQL(mySQL):
        CF.runSQL(mySQL)
