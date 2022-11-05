from sql import OutSet
from sql import InsSet
from JSON import ExpDataJson
from JSON import ImpDataJson
from JSON import ExpDataXml
from JSON import ImpDataXml

print("Управление справочником, для выбора необходимой команды, введите число: ")
while True:
    print("0 - Вывод данных таблицы\n"
          "1 - Добавление новой записи\n"
          "2 - Экспорт данных\n"
          "3 - Импорт данных\n"
          "4 - Завершение")
    usl = input("Ввод - ")
    if usl == "0":
        print(OutSet())
    elif usl == "1":
        name = input("Введите имя = ")
        number = int(input("Введите номер = "))
        InsSet(name, number)
    elif usl == "2":
        print("Введите формат экспорта\n"
              "0 - JSON\n"
              "1 - XML")
        form = input("Ввод - ")
        if form == "0":
            ExpDataJson()
        elif form == "1":
            ExpDataXml()
    elif usl == "3":
        print("Введите формат импорта\n"
              "0 - JSON\n"
              "1 - XML")
        form = input("Ввод - ")
        if form == "0":
            ImpDataJson()
        elif form == "1":
            ImpDataXml()
    elif usl == "4":
        break
    else:
        print("Неправильный ввод, повтори попытку)")
