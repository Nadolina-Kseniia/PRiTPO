import unittest

from lcd import lcd_digits


class TestLCDDigits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Считываем данные из текстового файла
        with open('input_lcd.txt', 'r') as file:
            cls.test_cases = [line.strip() for line in file.readlines()]

    def test_single_digit(self):
        # Тест для одного цифрового значения
        expected_output = ' -  \n  | \n -  \n|   \n -  '
        self.assertEqual(lcd_digits(self.test_cases[0], 1), expected_output)

    def test_multiple_digits(self):
        # Тест для нескольких цифровых значений
        expected_output = ' -   -  \n  |   | \n -   -  \n|     | \n -   -  '
        self.assertEqual(lcd_digits(self.test_cases[1], 1), expected_output)

    def test_large_size(self):
        # Тест для больших размеров
        expected_output = (' -----  \n'
                           '|     | \n'
                           '|     | \n'
                           '|     | \n'
                           '|     | \n'
                           '|     | \n'
                           '        \n'
                           '|     | \n'
                           '|     | \n'
                           '|     | \n'
                           '|     | \n'
                           '|     | \n'
                           ' -----  ')
        self.assertEqual(lcd_digits(self.test_cases[2], 5), expected_output)

    def test_invalid_input(self):
        # Тест для нецифрового ввода
        expected_output = '\n\n\n\n'
        self.assertEqual(lcd_digits(self.test_cases[3], 1), expected_output)

    def test_edge_case_zero(self):
        # Тест для граничного случая - 0
        expected_output = ' -  \n| | \n    \n| | \n -  '
        self.assertEqual(lcd_digits(self.test_cases[4], 1), expected_output)


if __name__ == '__main__':
    unittest.main()
