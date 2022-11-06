from sql import OutSet
from sql import InsSet
from sql import DelPers
from sql import PrintPers
from JSON import ExpDataJson
from JSON import ImpDataJson
from XML import ExpDataXml
from XML import ImpDataXml

print("Управление справочником, для выбора необходимой команды, введите число: ")
while True:
    print("0 - Вывод данных таблицы\n"
          "1 - Добавление новой записи\n"
          "2 - Вывод информации по конкретной персоне\n"
          "3 - Удаление информации по конкретной персоне\n"
          "4 - Экспорт данных\n"
          "5 - Импорт данных\n"
          "6 - Завершение")
    usl = input("Ввод - ")
    if usl == "0":
        print(OutSet())
    elif usl == "1":
        name = input("Введите имя = ")
        number = int(input("Введите номер = "))
        InsSet(name, number)
    elif usl == "2":
        print("Для вывода информации по человеку")
        name = input("Введите имя человека - ")
        print(PrintPers(name))
    elif usl == "3":
        name = input("Для удаление человека из справочника, введите имя - ")
        DelPers(name)
    elif usl == "4":
        print("Введите формат экспорта\n"
              "0 - JSON\n"
              "1 - XML")
        form = input("Ввод - ")
        if form == "0":
            ExpDataJson()
        elif form == "1":
            ExpDataXml()
    elif usl == "5":
        print("Введите формат импорта\n"
              "0 - JSON\n"
              "1 - XML")
        form = input("Ввод - ")
        if form == "0":
            ImpDataJson()
        elif form == "1":
            ImpDataXml()
    elif usl == "6":
        break
    else:
        print("Неправильный ввод, повтори попытку)")
