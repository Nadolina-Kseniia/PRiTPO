def can_arrange_teams(members, capacities):
    # Инициализируем список, в который будем записывать распределение
    seating_arrangement = [[] for _ in range(len(members))]

    # Параметр для общего количества мест
    total_seats = sum(capacities)

    # Сначала проверим, достаточно ли мест для всех участников
    total_members = sum(members)
    if total_members > total_seats:
        return (0, [])

    # Создаем список, который будет хранить "свободные" столы
    table_indices = []
    for i in range(len(capacities)):
        for _ in range(capacities[i]):
            table_indices.append(i + 1)  # Сохраняем номер стола

    # Заполняем распределение членов команды по столам
    idx = 0
    for team_idx, count in enumerate(members):
        for _ in range(count):
            # Если недостаточно мест, возвращаем 0
            if idx >= len(table_indices):
                return (0, [])
            seating_arrangement[team_idx].append(table_indices[idx])
            idx += 1

    return (1, seating_arrangement)


import sys

for line in sys.stdin:
    M, N = map(int, line.strip().split())
    if M == 0 and N == 0:
        break  # выход из цикла на ноль

    members = list(map(int, sys.stdin.readline().strip().split()))
    capacities = list(map(int, sys.stdin.readline().strip().split()))

    result, arrangement = can_arrange_teams(members, capacities)
    print(result)
    if result == 1:
        for tables in arrangement:
            print(' '.join(map(str, tables)))
