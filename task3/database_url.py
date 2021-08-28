import shelve
import main


def write_file_bin(add_url, short_url):
    with shelve.open(main.FILENAME) as f:
        f[short_url] = add_url
    f.close()


def get_url_date(get_url_name):
    with shelve.open(main.FILENAME) as f:
        res = f.get(get_url_name)
        if res is None:
            print(f'Данное значение {get_url_name} не найдено, повторите')
        else:
            print('*' * 5, "РЕЗУЛЬТАТ", '*' * 5)
            print(res, "\n")


def clear_database():
    with shelve.open(main.FILENAME) as f:
        f.clear()
        print('Список ссылок очищен', '\n')
