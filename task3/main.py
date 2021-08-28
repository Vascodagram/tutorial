import database_url

FILENAME = 'database/data'


def give_url():
    add_url = input('Введите ссылку: ')
    short_url = input('Введите сокращенное имя: ')
    database_url.write_file_bin(add_url, short_url)


def get_url():
    get_url_name = input('Введите название ссылки: ')
    database_url.get_url_date(get_url_name)


def main():
    while True:
        print('*' * 40)
        print('1 - Добавить ссылку')
        print('2 - Взять ссылку')
        print('3 - Удалить все ссылки из базы')
        print('4 - Выход')
        int_res = input('Введите значение: ')
        if int_res == "1":
            give_url()
        elif int_res == "2":
            get_url()
        elif int_res == "3":
            while True:
                yes_no_res = input("Вы точно хотите это сделать? yes/no: ")
                if yes_no_res == "yes":
                    database_url.clear_database()
                    break
                elif yes_no_res == "no":
                    break
                else:
                    pass
        elif int_res == "4":
            exit('Завершение программы.')
            print()
        else:
            print('Введено неверное значение, повторите попытку', '\n')


if __name__ == '__main__':
    main()
