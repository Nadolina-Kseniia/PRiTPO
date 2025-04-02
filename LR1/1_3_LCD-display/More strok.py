def lcd_digits(n, s):
    segments = {
        '0': [],
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': [],
    }

    # Определяем верхние, средние и нижние сегменты
    top = lambda d: ' ' + '-' * s + ' ' if d in '02356789' else ' ' * (s + 2)
    bottom = lambda d: ' ' + '-' * s + ' ' if d in '235689' else ' ' * (s + 2)

    # Определяем высоту сегментов
    middle = '|' + ' ' * s + '|'

    # Создание строк для верхней, средней и нижней части
    lines = []

    for digit in n:
        if digit not in '0123456789':
            continue

        # Входящие сегменты
        lines.append(top(digit))
        for i in range(s):
            lines.append(('|' if digit in '045689' else ' ') + ' ' * s + ('|' if digit in '01234789' else ' '))
        lines.append((' ' + '-' * s + ' ') if digit in '02345689' else ' ' * (s + 2))
        for i in range(s):
            lines.append(('|' if digit in '268' else ' ') + ' ' * s + ('|' if digit in '13456789' else ' '))
        lines.append(bottom(digit))
    #print(lines)
        lines.append('\n')
    # Объединяем строки и добавляем пробелы между цифрами
    return '\n'.join(lines)


def main():
    while True:
        line = input()
        s, n = map(int, line.split())
        if s == 0 and n == 0:
            break
        print(lcd_digits(str(n), s))


if __name__ == "__main__":
    main()
