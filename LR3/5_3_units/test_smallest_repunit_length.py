import pytest
from smallest_repunit_length import smallest_repunit_length

# Тестовые случаи из текстового файла
def load_test_cases():
    test_cases = []
    with open('test_data.txt', 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                n, expected = map(int, line.strip().split(','))
                test_cases.append((n, expected))
    return test_cases

# Основные тесты
@pytest.mark.parametrize("n, expected", [
    (1, 1),       # 1 делится на 1
    (3, 3),       # 111 делится на 3
    (7, 6),       # 111111 делится на 7
    (9, 9),       # 111111111 делится на 9
    (11, 2),      # 11 делится на 11
])
def test_smallest_repunit_length(n, expected):
    assert smallest_repunit_length(n) == expected

# Тесты с загруженными данными
@pytest.mark.parametrize("n, expected", load_test_cases())
def test_smallest_repunit_length_from_file(n, expected):
    assert smallest_repunit_length(n) == expected

# Тесты на исключения
def test_invalid_input():
    with pytest.raises(ValueError):
        smallest_repunit_length(2)   # кратно 2
    with pytest.raises(ValueError):
        smallest_repunit_length(5)   # кратно 5
    with pytest.raises(ValueError):
        smallest_repunit_length(10)  # кратно и 2 и 5