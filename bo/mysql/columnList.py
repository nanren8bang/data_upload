
import bo.mysql.column   as BO

class columnList:
    def __init__(self):
        self.BOList=[]
         
    def __str__(self):
        return "Hold column BO in List"

    def toCSV(self):
        tempString=''
        for i in self.BOList:
            tempString=tempString+i.toCSV()+'\n'
        return tempString


    def toCSV(self,file):
        writeFile=open(file,'w+')
        #writeFile.write(BO.report.getHeader())
        #writeFile.write('\n')
        for myBO in self.BOList:
            writeFile.write(myBO.toCSV())
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
