def decrypt_texts(cases):
    # Известный открытый текст и его структура
    plain_text = "the quick brown fox jumps over the lazy dog"
    plain_words = plain_text.split()
    plain_lengths = [len(word) for word in plain_words]

    results = []

    for current_case in cases:
        solution_found = False
        decryption_map = {}

        # Шаг 1: Найти, какая строка в current_case является шифровкой plain_text
        for line in current_case:
            words = line.split()
            if len(words) != len(plain_words):
                continue

            # Проверить длины слов
            valid_length = True
            for w, pl in zip(words, plain_lengths):
                if len(w) != pl:
                    valid_length = False
                    break
            if not valid_length:
                continue

            # Попробовать построить отображение
            temp_decryption = {}
            temp_encryption = {}
            valid_mapping = True

            for cipher_word, plain_word in zip(words, plain_words):
                if len(cipher_word) != len(plain_word):
                    valid_mapping = False
                    break
                for c_char, p_char in zip(cipher_word, plain_word):
                    if c_char in temp_decryption:
                        if temp_decryption[c_char] != p_char:
                            valid_mapping = False
                            break
                    else:
                        if p_char in temp_encryption:
                            if temp_encryption[p_char] != c_char:
                                valid_mapping = False
                                break
                        else:
                            temp_decryption[c_char] = p_char
                            temp_encryption[p_char] = c_char
                if not valid_mapping:
                    break

            if valid_mapping:
                decryption_map = temp_decryption
                solution_found = True
                break

        # Шаг 2: Расшифровать все строки
        if solution_found:
            decrypted_case = []
            for line in current_case:
                decrypted_line = []
                for char in line:
                    if char == ' ':
                        decrypted_line.append(' ')
                    elif char in decryption_map:
                        decrypted_line.append(decryption_map[char])
                    else:
                        decrypted_case = ["No solution."]
                        solution_found = False
                        break
                if not solution_found:
                    break
                decrypted_case.append(''.join(decrypted_line))
            if solution_found:
                results.append(decrypted_case)
            else:
                results.append(["No solution."])
        else:
            results.append(["No solution."])

    return results


def read_test_cases(file_path):
    cases = []
    with open(file_path, 'r') as file:
        current_case = []
        for line in file:
            line = line.strip()
            if not line:
                if current_case:
                    cases.append(current_case)
                    current_case = []
            else:
                current_case.append(line)
        if current_case:
            cases.append(current_case)
    return cases


def main():
    # Указываем фиксированный путь к файлу с тестами
    file_path = 'test_data.txt'
    test_cases = read_test_cases(file_path)
    results = decrypt_texts(test_cases)

    for i, result in enumerate(results):
        for line in result:
            print(line)
        if i < len(results) - 1:
            print()  # Пустая строка между блоками


if __name__ == "__main__":
    main()