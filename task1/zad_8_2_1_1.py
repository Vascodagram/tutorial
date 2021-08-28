def add_in_list_value(list_value):
    with open('test.txt', 'r') as f:
        while True:
            line_value = f.readline()
            clear_line = line_value.rstrip()
            if not line_value:
                break
            else:
                list_value.append(int(clear_line))
    f.close()


def main():
    list_value = []
    add_in_list_value(list_value)
    print(sum(list_value))


if __name__ == '__main__':
    main()