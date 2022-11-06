import os
import xml.etree.ElementTree as ET
from sql import OutSet
from sql import InsSet

def ExpDataXml():
    Phonebook = ET.Element("Phonebook")
    data = OutSet()
    fileName = "Phonebook.xml"
    dirName = "export_files"

    for i in range(0, len(data)):
        Phonebook.set(data[i][0], data[i][1])

    xmlData = ET.tostring(Phonebook, encoding='unicode')
    path = os.path.join(dirName, fileName)
    file = open(path, "w")
    file.write(xmlData)

def ImpDataXml():
    dirName = "import_files"
    fileName = input("Введите название файла - ")
    path = os.path.join(dirName, fileName)
    allData = ET.parse(path)
    data = allData.getroot()
    print(data[0])

ImpDataXml()

