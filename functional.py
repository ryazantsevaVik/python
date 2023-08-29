def add_person(person):
    data = open('data.txt', 'a', encoding='utf-8')
    data.write(person)
    data.write('\n')
    data.close()

def show_all():
    data = open ('data.txt', 'r', encoding ='utf-8')
    for line in data:
        print(line[:-1])
    data.close()

def search_element(name):
    with open ('data.txt', 'r', encoding ='utf-8') as data:
        for line in data:
            if name in line:
                print(line[:-1])
   

def change_element(name):
    with open ('data.txt', 'r+', encoding ='utf-8') as data:
        new_data = data.readlines()
        with open('data.txt', 'w+', encoding='utf-8') as data:
            for line in new_data:
                if name in line:
                    data.write(input('Введите новые данные: '))
                    data.write('\n')
                    print("Данные изменены")
                    data.close()
                else:
                    data.write(line)

def delete_element(name):
    with open('data.txt', 'r', encoding='utf-8') as data:
        new_data = data.readlines()
    with open('data.txt', 'w+', encoding='utf-8') as data:
        for line in new_data:
            if name not in line:
                data.write(line)
                