
import bo.general_properties   as BO

class general_propertiesList:
    def __init__(self):
        self.reportList=[]
         
    def __str__(self):
        return "Hold general_properties Value BO in a List"

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
        writeFile=open(file,'w+')
        #writeFile.write(BO.report.getHeader())
        #writeFile.write('\n')
        for myBO in self.reportList:
            writeFile.write(myBO.toTSV())
        writeFile.close()

    def toCSVHeader(self,file):
        writeFile=open(file,'w+')
        writeFile.write(BO.general_properties.getHeaderCSV())
        writeFile.close()

    def toTSVHeader(self,file):
        writeFile=open(file,'w+')
        writeFile.write(BO.general_properties.getHeaderTSV())
        writeFile.close()
