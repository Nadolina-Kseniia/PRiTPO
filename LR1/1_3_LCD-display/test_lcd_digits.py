import unittest

from lcd import lcd_digits

class TestLCDDigits(unittest.TestCase):

    def test_single_digit(self):
        # Тест для одного цифрового значения
        expected_output = ' -  \n  | \n -  \n|   \n -  '
        self.assertEqual(lcd_digits('2', 1), expected_output)

    def test_multiple_digits(self):
        # Тест для нескольких цифровых значений
        expected_output = ' -   -  \n  |   | \n -   -  \n|     | \n -   -  '
        self.assertEqual(lcd_digits('23', 1), expected_output)

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
        self.assertEqual(lcd_digits('0', 5), expected_output)

    def test_invalid_input(self):
        # Тест для нецифрового ввода
        expected_output = '\n\n\n\n'
        self.assertEqual(lcd_digits('a', 1), expected_output)

    def test_edge_case_zero(self):
        # Тест для граничного случая - 0
        expected_output = ' -  \n| | \n    \n| | \n -  '
        self.assertEqual(lcd_digits('0', 1), expected_output)


if __name__ == '__main__':
    unittest.main()