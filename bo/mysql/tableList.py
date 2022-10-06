
import bo.table   as BO

class tableList:
    def __init__(self):
        self.BOList=[]
         
    def __str__(self):
        return "Hold table BO in List"

    def toCSV(self):
        tempString=''
        for i in self.BOList:
            tempString=tempString+i.toCSV()+'\n'
        return tempString


    def toCSV(self,file):
        writeFile=open(file,'w+')
        for myBO in self.BOList:
            writeFile.write(myBO.toCSV())
        writeFile.close()
    def toTSV(self,file):
        writeFile=open(file,'w+')
        for myBO in self.BOList:
            writeFile.write(myBO.toTSV())
        writeFile.close()

    def toCSVHeader(self,file):
        writeFile=open(file,'w+')
        writeFile.write(BO.table.getHeaderCSV())
        writeFile.close()

    def toTSVHeader(self,file):
        writeFile=open(file,'w+')
        writeFile.write(BO.table.getHeaderTSV())
        writeFile.close()


