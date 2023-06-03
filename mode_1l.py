def add_cont(new_contact, phonenumber):
    data = open('Phonebook.txt', 'a')
    data.write(new_contact + " " + phonenumber + "\n")
    data.close()


def show_all():
    data = open('Phonebook.txt', "r")
    for line in data:
        print(line[:-1])
    data.close()


def search(stroka):
    a = 0
    data = open('Phonebook.txt', 'r')
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        print("Контакт не найден")
    data.close()


def change(file_name, old_value):
    with open(file_name, "r+") as data1:
        contents = data1.read()
        new_value = input('Введите новое значение: ')
        contents = contents.replace(old_value, new_value)
        with open(file_name, "w") as data2:
            data2.write(contents)


def delete_contact(file_name, old_value):
    with open(file_name, "r+") as data1:
        contents = data1.read().splitlines()
        for line in contents:
            if old_value in line:
                contents.remove(line)
            else:
                print('Такого элемента нет.')
            with open(file_name, "w") as data2:
                for i in contents:
                    data2.write(i)
                    data2.write('\n')


def create(base):
    try:
        file = open(base, 'r')
    except IOError:
        print('Создан новый справочник -> phonebook.txt ')
        file = open(base, 'w')
    finally:
        file.close()
        