import os
import json
from sql import OutSet
from sql import InsSet

def ExpDataJson():
    di = {}
    data = OutSet()
    fileName = "Phonebook.json"
    dirName = "export_files"

    for i in range(0, len(data)):
        di[data[i][0]] = data[i][1]

    jsonData = json.dumps({"Phonebook": di})
    path = os.path.join(dirName, fileName)
    with open(path, "w") as file:
        json.dump(jsonData, file)

def ImpDataJson():
    dirName = "import_files"
    fileName = input("Введите название файла - ")
    path = os.path.join(dirName, fileName)
    with open(path, "r") as file:
        jsonData = json.load(file)
    jsonData = json.loads(jsonData)
    for i, j in jsonData['Phonebook'].items():
        InsSet(i, j)
    print(type(jsonData))

#ExpDataJson()
#ImpDataJson()
