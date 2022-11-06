import os
import xml.etree.ElementTree as ET
from sql import OutSet
from sql import InsSet

def ExpDataXml():
    root = ET.Element("Phonebook")
    data = OutSet()
    fileName = "Phonebook.xml"
    dirName = "export_files"

    for i in range(0, len(data)):
        pers = ET.SubElement(root, "pers")
        pers.set("id", str(i))
        name = ET.SubElement(pers, "name")
        name.text = data[i][0]
        number = ET.SubElement(pers, "number")
        number.text = str(data[i][1])

    xmlData = ET.tostring(root, encoding='unicode')
    path = os.path.join(dirName, fileName)
    file = open(path, "w")
    file.write(xmlData)
    file.close()

def ImpDataXml():
    dirName = "import_files"
    fileName = "Phonebook.xml" #input("Введите название файла - ")
    path = os.path.join(dirName, fileName)
    tree = ET.parse(path)
    root = tree.getroot()
    for i in range(0, len(root)):
        InsSet(root[i][0].text, int(root[i][1].text))