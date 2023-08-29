from interface import *
from functional import *

while True:
    base_menu()
    command = int(input('Введите команду: '))
    if command == 1:
        person = input("Введите ФИО и номер телефона: \n")
        add_person(person)
    elif command == 2:
        show_all()
    elif command == 3:
        name = input("Введите фамилию и имя для поиска: \n")
        search_element(name)
    elif command == 4:
        old_name = input("Введите фамилию и имя контакта, который хотите изменить: \n")
        change_element(old_name)
    elif command == 5:
        name = input("Введите фамилию и имя контакта, который хотите удалить: \n")
        delete_element(name)
    elif command == 6:
        break
    else:
        print("Ввод некорректен")