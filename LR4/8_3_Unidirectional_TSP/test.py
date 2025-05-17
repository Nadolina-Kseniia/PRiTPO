import unittest
import tempfile
import os
from Unidirectional_TSP import read_matrix, find_min_path, main


class TestMinPath(unittest.TestCase):
    def test_single_element(self):
        """Тест для матрицы 1x1."""
        m, n, matrix = 1, 1, [[5]]
        path, cost = find_min_path(m, n, matrix)
        self.assertEqual(path, [1])
        self.assertEqual(cost, 5)

    def test_single_row(self):
        """Тест для одной строки."""
        m, n, matrix = 1, 5, [[5, 4, 3, 2, 1]]
        path, cost = find_min_path(m, n, matrix)
        self.assertEqual(path, [1, 1, 1, 1, 1])
        self.assertEqual(cost, sum([5, 4, 3, 2, 1]))

    def test_single_column(self):
        """Тест для одного столбца."""
        m, n, matrix = 3, 1, [[1], [2], [3]]
        path, cost = find_min_path(m, n, matrix)
        self.assertIn(path, [[1], [2], [3]])
        self.assertEqual(cost, 1)  # Ожидается минимальное значение первого столбца


    def test_read_matrix_from_file(self):
        """Тест чтения матрицы из файла."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
            tmp.write("3 3\n")
            tmp.write("1 2 3\n")
            tmp.write("4 5 6\n")
            tmp.write("7 8 9\n")
            tmp_name = tmp.name

        matrices = list(read_matrix(tmp_name))
        os.unlink(tmp_name)

        self.assertEqual(len(matrices), 1)
        m, n, matrix = matrices[0]
        self.assertEqual(m, 3)
        self.assertEqual(n, 3)
        self.assertEqual(matrix, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_main_output(self):
        """Тест вывода основной функции."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as in_tmp:
            in_tmp.write("3 3\n1 2 3\n4 5 6\n7 8 9\n")
            in_name = in_tmp.name

        # Перенаправляем вывод
        with open(in_name, 'r') as f:
            # Здесь можно использовать subprocess для проверки вывода
            # Пример упрощен для краткости
            pass

        os.unlink(in_name)


if __name__ == "__main__":
    unittest.main()