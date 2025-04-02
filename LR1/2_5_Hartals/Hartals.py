"""Надолина К.Р. ИВТ-233"""


def count_lost_working_days(N, params):
    """ Проверка на корректность входных данных """
    if not (isinstance(N, int) and 7 <= N <= 3650):
        return ''

    """ Определяем P как длину списка params """
    P = len(params)
    if not (isinstance(P, int) and 1 <= P <= 100):
        return ''
    if not isinstance(params, list) or len(params) != P:
        return ''

    lost_days = set()

    for A in params:
        if not (isinstance(A, int) and A > 0 and A <= 100 and A % 7 != 0):
            return ''

        day = A
        while day <= N:
            if (day % 7) != 6 and (day % 7) != 0:
                lost_days.add(day)
            day += A

    return len(lost_days)


data = input().split()

T = int(data[0])
results = []

index = 1
for _ in range(T):
    N = int(data[index])
    P = int(data[index + 1])
    params = list(map(int, data[index + 2:index + 2 + P]))

    lost_days_count = count_lost_working_days(N, params)
    results.append(lost_days_count)

    index += 2 + P  # Обновляем индекс для следующего теста

    """входные данные
    2 14 3 3 4 8 100 4 12 15 25 40
    выходные данные
    5 15"""

print(*results)
