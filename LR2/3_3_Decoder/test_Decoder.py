import pytest
from Decoder import decrypt_texts


# Проверяет корректную расшифровку на примере, где зашифрованный текст соответствует
# известной фразе. Ожидается, что функция восстановит маппинг и вернет исходные строки.
def test_valid_decryption():
    cases = [
        [
            ["gsv jfrxp yilzw", "nfyb qnweql"]
        ]
    ]
    expected = [
        ["the quick brown", "lazy dog jumps"]
    ]
    assert decrypt_texts(cases) == expected


#Случай, когда маппинг невозможен из-за отсутствия подходящих слов в known_words.
# Ожидается "No solution.".
def test_no_solution():
    cases = [
        [
            ["abc def"],  # Нет подходящих слов в known_words
            ["xyz"]
        ]
    ]
    expected = [["No solution."]]
    assert decrypt_texts(cases) == expected

#После успешного маппинга в строке встречается символ, отсутствующий в маппинге.
# Функция должна вернуть "No solution.".
def test_unmapped_char_in_line():
    cases = [
        [
            ["gsv jfrxp"],  # Маппинг найден для "gsv" -> "the", "jfrxp" -> "quick"
            ["abcx"]        # 'x' не участвовал в маппинге
        ]
    ]
    expected = [["No solution."]]
    assert decrypt_texts(cases) == expected

# Обработка нескольких независимых случаев. Проверяет, что каждый случай обрабатывается отдельно.
def test_multiple_cases():
    cases = [
        [["gsv jfrxp"]],           # Valid
        [["invalid"]],             # No solution
        [["gsvx"]]                 # Unmapped 'x'
    ]
    expected = [
        ["the quick"],            # Case 1
        ["No solution."],          # Case 2
        ["No solution."]           # Case 3
    ]
    assert decrypt_texts(cases) == expected

# Пустой входной случай. Функция возвращает "No solution.".
def test_empty_case():
    cases = [[]]
    expected = [["No solution."]]
    assert decrypt_texts(cases) == expected

#Конфликт в маппинге (например, длина слов не совпадает с known_words).
# Ожидается "No solution.".
def test_conflicting_mapping():
    cases = [
        [
            ["ab", "cd"],  # Нет слов длины 2 в known_words ("the", "quick", ...)
        ]
    ]
    expected = [["No solution."]]
    assert decrypt_texts(cases) == expected