def min_stations(cities, city_pairs):
    # Создаем список смежности для графа
    graph = [[] for _ in range(cities + 1)]

    # Заполняем граф на основе входных рёбер
    for first_city, second_city in city_pairs:
        graph[first_city].append(second_city)
        graph[second_city].append(first_city)

    # Массив для отслеживания, установлена ли станция в городе
    visited = [False] * (cities + 1)
    stations = 0

    # Проходим по всем городам
    for town in range(1, cities + 1):
        if not visited[town]:  # Если в городе еще нет станции
            # Устанавливаем станцию в текущем городе
            stations += 1
            visited[town] = True  # Отмечаем, что в этом городе есть станция

            # Отмечаем соседние города как обслуживаемые
            for neighbor in graph[town]:
                visited[neighbor] = True

    return stations


# Чтение входных данных
import sys

for line in sys.stdin:
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break

    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))

    # Вызываем функцию и выводим результат
    result = min_stations(n, edges)
    print(result)
