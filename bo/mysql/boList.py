
#import bo.mysql.column   as BO

class boList:
    def __init__(self):
        self.BOList=[]
         
    def __str__(self):
        return "Hold column BO in List"

    def toCSV(self):
        tempString=''
        for i in self.BOList:
            tempString=tempString+i.toCSV()+'\n'
        return tempString


    def toTupleList(self):
        tempStr='['
        
        for myBO in self.BOList:
            tempStr=tempStr+'\n('+myBO.toCSV()+'),'
        tempStr=tempStr[:-1] #<----remove last comma
        tempStr=tempStr+'\n]'
        return tempStr


    def toCSV(self,file):
        writeFile=open(file,'w+')
        #writeFile.write(BO.report.getHeader())
        #writeFile.write('\n')
        for myBO in self.BOList:
            writeFile.write(myBO.toCSV()) #make sure change the encoded in  utf8
            #writeFile.write(myBO.toCSV().encode('utf8')) #make sure change teh encode to utf8
        writeFile.close()
    def toTSV(self,file):
        writeFile=open(file,'w+')
        #writeFile.write(BO.report.getHeader())
        #writeFile.write('\n')
        for myBO in self.BOList:
            writeFile.write(myBO.toTSV())
        writeFile.close()

    def toCSVHeader(self,file):
        writeFile=open(file,'w+')
        writeFile.write(BO.columnDataType.getHeaderCSV())
        writeFile.close()

    def toTSVHeader(self,file):
        writeFile=open(file,'w+')
        writeFile.write(BO.columnDataType.getHeaderTSV())
        writeFile.close()
"""
    def toTupleList(self,file):
        writeFile=open(file,'w+')
        #writeFile.write(BO.report.getHeader())
        writeFile.write('[')
        for myBO in self.BOList:
            writeFile.write('('+myBO.toCSV()+'),')
        writeFile.write(']')
        writeFile.close()
"""
