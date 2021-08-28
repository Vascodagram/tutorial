import random
import zad_8_2_1_1 as sum_module


def create_value():
    with open('test.txt', 'w') as f:
        for _ in range(1, 10001):
            result = random.randint(1, 999999999999)
            f.write(str(result) + '\n')
        f.close()
        print('Программа выполнена успешно')


def output_value():
    try:
        sum_module.main()
    except FileNotFoundError as error:
        print('Файл не найден, повторите попытку', '\n')
        main()


def main():
    print('1 - Записать 10000 случайных чисел')
    print('2 - Вывести сумму 10000 случайных чисел')
    print('3 - Выйти', '\n')
    input_value = input('Выберите 1/2/3: ')
    if input_value == '1':
        create_value()
    elif input_value == '2':
        output_value()
    elif input_value == '3':
        exit('Выход из программы')
    else:
        print('Повторите попытку')


if __name__ == '__main__':
    main()
