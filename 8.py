def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')

def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename) 
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)    
    for i in range(1,len(data_array)):
        print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1],"Имя: ", data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])

def edit_an_entry(filename):
    data_array = read_file(filename)
    print('Введите ID записи которую хотите изменить: ')
    show_all_items(filename)
    id = input()
    for i in range(1,len(data_array)):
        if data_array[i][0] == id:
            print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1],"Имя: ", data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])
            temp = i
    print('Введите что хотите изменить: ')
    print('1 - Фамилия')
    print('2 - Имя')
    print('3 - Отчество')
    print('4 - Телефон')
    id_chenge = input()
    new_data = input('Введите новое значение: ')
    if int(id_chenge) == 1:
        data_array[temp][1] = new_data
    elif int(id_chenge) == 2:
        data_array[temp][2] = new_data
    elif int(id_chenge) == 3:
        data_array[temp][3] = new_data
    elif int(id_chenge) == 4:
        data_array[temp][4] = new_data
    write_file(filename, data_array)

def delete_item(filename):
    data_array = read_file(filename)
    print('Введите ID записи которую хотите удалить: ')
    show_all_items(filename)
    id = input()
    for i in range(1,len(data_array)):
        if data_array[i][0] == id:
            temp = i
            print('Вы точно хотите удалить данную запись?')
            print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1],"Имя: ", data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])
            print('Введите "Да" или для продолжения, либо "Нет" для отмены: ')
            user_input = input()
            if user_input == "Да":
                data_array.remove(data_array[i])
            write_file(filename, data_array)
def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3:
        edit_an_entry(filename)
    elif user_operation == 4:
        delete_item(filename)

filename = 'file.txt'
menu()