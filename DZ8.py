def show_data():
    """Функция выводит контакты"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()#.split('\n')
    return book

def find_data():
    """Функция ищет контакты"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('что ищем?: ')
        for i in book:
            if temp in i:
                print(i)

def new_data():
    """Функция добавляет добавляет контакты"""
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )
    
def delete_person(name):
    """Функция удаляет контакты"""
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
    """Функция изменяет контакты"""
    persons = read_data()
    with open("data.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")
while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('кого удаляем?: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('кого хотим переименовать?: ')
        new_name = input('как хотим его назвать?: ')
        change_person(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('No mode')
