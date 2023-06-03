def start():
    pass
    view.welcome()
    path = "Phonebook.txt"
    model.create(path)
    while True:
        choice = view.interface()
        if choice == 0 or choice > 6:
            view.error()
        elif choice == 1:
            contact = input('Введите имя и фамилию контакта: ')
            phonenumber = input('Введите телефонный номер контакта: ')
            model.add_cont(contact, phonenumber)
            view.ok()
        elif choice == 2:
            model.show_all()
        elif choice == 3:
            find = input('Введите Фамилию или номер контакта: ')
            model.search(find)
        elif choice == 4:
            fam = input('Введите текст для редактирования: ')
            model.change(path, fam)
        elif choice == 5:
            delcont = input('Введите строку для удаления: ')
            model.delete_contact(path, delcont)
        elif choice == 6:
            view.goodbye()
            break