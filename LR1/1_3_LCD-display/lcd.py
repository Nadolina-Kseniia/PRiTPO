""" Надолина К.Р. ИВТ-233 """


def get_top_segment(digit, size):
    return ' ' + '-' * size + ' ' if digit in '02356789' else ' ' * (size + 2)


def get_middle_segment(digit, size):
    return ' ' + '-' * size + ' ' if digit in '2345689' else ' ' * (size + 2)


def get_bottom_segment(digit, size):
    return ' ' + '-' * size + ' ' if digit in '0235689' else ' ' * (size + 2)


def lcd_digits(n, s):
    # Создание строк для верхней, средней и нижней части
    lines = []
    top_lines = []
    middle_t_lines = []
    middle_lines = []
    middle_b_lines = []
    bottom_lines = []

    for digit in n:
        if digit not in '0123456789':
            continue

        # Входящие сегменты
        lines.append(get_top_segment(digit, s))
        top_lines.append(get_top_segment(digit, s) + ' ')

        middle_t_lines.append(
            ('|' if digit in '045689' else ' ') + ' ' * s +
            ('|' if digit in '01234789' else ' ')
        )
        middle_t_lines.append(' ')

        for _ in range(s):
            lines.append(
                ('|' if digit in '045689' else ' ') + ' ' * s +
                ('|' if digit in '01234789' else ' ')
            )

        lines.append(get_middle_segment(digit, s))
        middle_lines.append(get_middle_segment(digit, s) + ' ')

        middle_b_lines.append(
            ('|' if digit in '0268' else ' ') + ' ' * s +
            ('|' if digit in '013456789' else ' ')
        )
        middle_b_lines.append(' ')

        for _ in range(s):
            lines.append(
                ('|' if digit in '0268' else ' ') + ' ' * s +
                ('|' if digit in '013456789' else ' ')
            )

        lines.append(get_bottom_segment(digit, s))
        bottom_lines.append(get_bottom_segment(digit, s) + ' ')

    # Объединяем строки и добавляем пробелы между цифрами
    result_lines = []
    result_lines.append(''.join(top_lines))
    for _ in range(s):
        result_lines.append(''.join(middle_t_lines))
    result_lines.append(''.join(middle_lines))
    for _ in range(s):
        result_lines.append(''.join(middle_b_lines))
    result_lines.append(''.join(bottom_lines))

    return '\n'.join(result_lines)


def main():
    while True:
        line = input()
        s, n = map(int, line.split())
        if s == 0 and n == 0:
            break
        print(lcd_digits(str(n), s))


if __name__ == "__main__":
    main()
