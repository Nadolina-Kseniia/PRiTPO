# test_Decoder.py

from Decoder import decrypt_texts

def run_tests():
    test_cases = [
        # Тест 1: Простой случай
        [
            ["gsv jfrxp ybgsrh"],
            ["nfyb qnweql"]
        ],
        # Тест 2: Похожая структура
        [
            ["odg ql jfw irexg frtzo"],
            ["sbw xm nq"]
        ],
        # Тест 3: Сложный случай
        [
            ["lyb gvcob gsxi ghupr"],
            ["nq mv",
             "qs"
            ]
        ],
        # Тест 4: Нет решения
        [
            ["xyz abc"],
            ["agh bcd"]
        ],
        # Тест 5: Полное соответствие
        [
            ["the quick brown fox"],
            ["jumps over the lazy dog"]
        ],
    ]

    for i, test_case in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        results = decrypt_texts(test_case)  # Используем функцию из Decoder.py
        for line in results:
            print(line)
        print()  # Пустая строка между тестами


if __name__ == "__main__":
    run_tests()
