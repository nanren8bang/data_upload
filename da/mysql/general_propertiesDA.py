import bo.general_properties      as BO
import da.mysqlDispatch.connectionFactory4Dispatch as CF
class general_propertiesDA:

    ##1: C 


    ##2: R 


    @staticmethod       
    def getArchiveProtectedGroups():
        myBOList=[]
        mySQL="""
              SELECT * 
              FROM dispatch.general_properties gp 
              WHERE gp.key='GroupsProtectedFromArchival' 
                AND (effective_date IS NULL OR effective_date<=CURDATE()) 
                AND (expiration_date IS NULL OR expiration_date>=CURDATE()) 
                AND (env IS NULL OR env='ALL' )
           
			""" 

        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.general_properties.fromTuple(result))
        return myBOList
    
    @staticmethod       
    def getAll():
        myBOList=[]
        mySQL="""
              SELECT * from dispatch.general_properties
	      """ 

        results=CF.connectionFactory4Dispatch.runSelect(mySQL)
        for result in results:
            myBOList.append(BO.dispatch.general_properties.fromTuple(result))
        return myBOList
    

    ##3: U of CRUD
    ##4: D of CRUD

    ##5: misc
    @staticmethod       
    def runSQL(mySQL):
        CF.connectionFactory4Dispatch.runSQL(mySQL)
   
 

