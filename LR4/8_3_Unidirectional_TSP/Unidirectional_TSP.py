def read_matrix(file_path):
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            m, n = map(int, line.split())
            matrix = [list(map(int, file.readline().split())) for _ in range(m)]
            yield m, n, matrix
def find_min_path(m, n, matrix):
    # Создаем список для хранения минимальных путей для каждого столбца
    paths = [[(matrix[i][0], i)] for i in range(m)]
    # Перебираем столбцы матрицы, начиная со второго
    for j in range(1, n):
        new_paths = []
        for i in range(m):
            # Выбираем минимальный путь из возможных предыдущих шагов
            options = [paths[(i - 1) % m], paths[i], paths[(i + 1) % m]]
            min_path = min(options, key=lambda x: matrix[x[-1][1]][j - 1] + x[-1][0])
            # Добавляем текущий шаг к выбранному пути
            new_paths.append(min_path + [(matrix[i][j], i)])
        paths = new_paths
    # Находим путь с минимальной суммой весов
    min_weight_path = min(paths, key=lambda x: sum(weight for weight, _ in x))
    # Возвращаем путь и его вес
    return [i + 1 for _, i in min_weight_path], sum(weight for weight, _ in min_weight_path)
def main():
    # Пример чтения данных из файла и вывода результата
    for m, n, matrix in read_matrix('input5.txt'):
        path, cost = find_min_path(m, n, matrix)
        print(' '.join(map(str, path)))
        print(cost)
if __name__ == "__main__":
    main()
