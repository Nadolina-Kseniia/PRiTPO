def count_numbers(numbers):
    # Создаем массив dp, где dp[i] будет хранить количество чисел,
    # сумма цифр которых равна i.
    dp = [0] * (numbers + 1)

    # Базовый случай: есть один способ получить сумму 0 (пустое число)
    dp[0] = 1

    # Цифры, которые Густаво знает.
    digits = [1, 2, 3, 1]  # 4 заменяем на 1

    # Проходим по всем возможным суммам от 1 до n
    for i in range(1, numbers + 1):
        # Для каждой суммы пробуем все известные Густаво цифры
        for digit in digits:
            if digit <= i:  # Если цифра меньше или равна текущей сумме
                dp[i] += dp[i - digit]  # Добавляем количество способов для оставшейся суммы

    return dp[numbers]


# Читаем входные данные до конца файла
import sys

# Будем хранить результаты
results = []

for line in sys.stdin:
    n = int(line.strip())
    results.append(count_numbers(n))

# Выводим результаты
for result in results:
    print(result)
