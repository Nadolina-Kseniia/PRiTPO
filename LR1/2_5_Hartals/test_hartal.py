import unittest
def count_lost_working_days(N, params):
    # Проверка на корректность входных данных
    if not (isinstance(N, int) and 7 <= N <= 3650):
        return ''  # Возвращаем пустую строку для некорректного ввода

    P = len(params)  # Определяем P как длину списка params
    if not (isinstance(P, int) and 1 <= P <= 100):
        return ''  # Возвращаем пустую строку, если P некорректно
    if not isinstance(params, list) or len(params) != P:
        return ''  # Возвращаем пустую строку, если список params не соответствует P

    lost_days = set()

    for A in params:
        if not (isinstance(A, int) and A > 0 and A <= 100 and A % 7 != 0):
            return ''  # Возвращаем пустую строку, если параметр некорректен

        day = A
        while day <= N:
            if (day % 7) != 6 and (day % 7) != 0:
                lost_days.add(day)
            day += A

    return len(lost_days)

class TestLostWorkingDays(unittest.TestCase):

    #1. Тесты на корректные входные данные
    #Тест с обычными значениями
    def test_case_1(self):
        N = 14
        params = [3, 4, 8]
        expected = 5  # Ожидаемый результат
        result = count_lost_working_days(N, params)
        self.assertEqual(result, expected)

    #Тест с максимальным значением N
    def test_case_2(self):
        N = 3650
        params = [1, 2, 3]
        expected = 2608  # Ожидаемый результат
        result = count_lost_working_days(N, params)
        self.assertEqual(result, expected)

    #2. Тесты на некорректные входные данные
    #Тест с некорректным значением N
    def test_case_3(self):
        N = 6
        params = [1]
        expected = ''  # Ожидаемый результат
        result = count_lost_working_days(N, params)
        self.assertEqual(result, expected)

    #Тест с некорректным значением P
    def test_case_4(self):
        N = 14
        params = []
        expected = ''  # Ожидаемый результат
        result = count_lost_working_days(N, params)
        self.assertEqual(result, expected)

    #Тест с некорректными параметрами
    def test_case_5(self):
        N = 14
        params = [105]
        expected = ''  # Ожидаемый результат
        result = count_lost_working_days(N, params)
        self.assertEqual(result, expected)

    #3. Граничные условия
    #Тест с минимальными значениями
    def test_case_6(self):
        N = 7
        params = [1]
        expected = 5  # Ожидаемый результат
        result = count_lost_working_days(N, params)
        self.assertEqual(result, expected)

    #4. Тесты на производительность
    #Тест с большим количеством параметров
    def test_case_7(self):
        N = 3650
        params = [1]*100 # 100 параметров, все равны 1
        expected = 2608  # Ожидаемый результат
        result = count_lost_working_days(N, params)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()