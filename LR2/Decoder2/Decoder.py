def decrypt_blocks(input_data):
    # Известный открытый текст
    known_plain_text = "the quick brown fox jumps over the lazy dog"

    # Функция для получения возможного соответствия
    def find_mapping(encrypted_line):
        mapping = {}
        reverse_mapping = {}
        words = encrypted_line.split()

        # Проверяем каждую строку
        for known_word in known_plain_text.split():
            if not words:
                return None
            encrypted_word = words.pop(0)

            if len(encrypted_word) != len(known_word):
                return None

            for e_char, k_char in zip(encrypted_word, known_word):
                if e_char in mapping:
                    if mapping[e_char] != k_char:
                        return None
                else:
                    mapping[e_char] = k_char

                if k_char in reverse_mapping:
                    if reverse_mapping[k_char] != e_char:
                        return None
                else:
                    reverse_mapping[k_char] = e_char

        return mapping

    # Функция для расшифровки строки
    def decrypt_line(line, mapping):
        decrypted = []
        for char in line:
            if char in mapping:
                decrypted.append(mapping[char])
            else:
                decrypted.append(char)  # пробелы остаются без изменений
        return ''.join(decrypted)

    # Обработка входных данных
    blocks = input_data.strip().split('\n\n')
    results = []

    for block in blocks:
        lines = block.strip().split('\n')[1:]  # Игнорируем первую строку
        if len(lines) > 100:  # Ограничение на количество строк
            results.append("No solution")
            continue

        found_solution = False

        for line in lines:
            # Проверка на допустимые символы и длину строки
            if any(c not in "abcdefghijklmnopqrstuvwxyz " for c in line) or len(line) > 80:
                results.append("No solution")
                found_solution = True
                break

            mapping = find_mapping(line)
            if mapping:
                found_solution = True
                decrypted_lines = [decrypt_line(l, mapping) for l in lines]
                results.append('\n'.join(decrypted_lines))
                break

        if not found_solution:
            results.append("No solution")

    return '\n\n'.join(results)


# Пример использования
input_data = """1
vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq
xnm ceoub lrtzv ita hegfd tsmr xnm ypwq ktj
frtjrpgguvj otvxmdxd prm iev prmvx xnmq"""

output = decrypt_blocks(input_data)
print(output)
