import os
import bo.report   as BO

class reportList:
    def __init__(self):
        self.reportList=[]
         
    def __str__(self):
        return "Hold report Value BO in a List"

    def toCSV(self):
        tempString=''
        for i in self.reportList:
            tempString=tempString+i.toCSV()+'\n'
        return tempString

    def toCSV(self,file):
        writeFile=open(file,'w+')
        #writeFile.write(BO.report.getHeader())
        #writeFile.write('\n')
        for myBO in self.reportList:
            writeFile.write(myBO.toCSV())
        writeFile.close()

    def toTSV(self,file):
        if os.path.exists(file):
            os.remove(file)

        writeFile=open(file,'w+')
        #writeFile.write(BO.report.getHeader())
        #writeFile.write('\n')
        for myBO in self.reportList:
            writeFile.write(myBO.toTSV())
        writeFile.close()
    def toCSVHeader(self,file):
        writeFile=open(file,'w+')
        writeFile.write(BO.report.getHeaderCSV())
        writeFile.close()

    def toTSVHeader(self,file):
        writeFile=open(file,'w+')
        writeFile.write(BO.report.getHeaderTSV())
        writeFile.close()
