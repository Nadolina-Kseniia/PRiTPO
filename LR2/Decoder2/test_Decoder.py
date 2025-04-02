def decrypt_blocks_from_file(filename):
    with open(filename, 'r') as file:
        input_data = file.read()

    return decrypt_blocks(input_data)


def decrypt_blocks(input_data):
    known_plain_text = "the quick brown fox jumps over the lazy dog"

    def find_mapping(encrypted_line):
        mapping = {}
        reverse_mapping = {}
        encrypted_words = encrypted_line.split()
        known_words = known_plain_text.split()

        if len(encrypted_words) != len(known_words):
            return None

        for enc_word, known_word in zip(encrypted_words, known_words):
            if len(enc_word) != len(known_word):
                return None
            for enc_char, known_char in zip(enc_word, known_word):
                if enc_char in mapping:
                    if mapping[enc_char] != known_char:
                        return None
                else:
                    mapping[enc_char] = known_char

                if known_char in reverse_mapping:
                    if reverse_mapping[known_char] != enc_char:
                        return None
                else:
                     reverse_mapping[known_char] = enc_char
        return mapping


    def decrypt_line(line, mapping):
        decrypted = []
        for char in line:
            decrypted.append(mapping.get(char, char)) # используем get для дефолтных символов
        return ''.join(decrypted)

    blocks = input_data.strip().split('\n\n')
    results = []

    for block in blocks:
        lines = block.strip().split('\n')
        block_id = lines[0] # Сохраняем идентификатор блока
        encrypted_lines = lines[1:]

        if len(encrypted_lines) > 100\
                or any(len(line) > 80 for line in encrypted_lines) or\
                any(any(c not in "abcdefghijklmnopqrstuvwxyz " for c in line) for\
                    line in encrypted_lines):
            results.append(f"{block_id}\nNo solution")
            continue


        mapping = find_mapping(encrypted_lines[0])

        if mapping:
            decrypted_lines = [decrypt_line(line, mapping) for line in encrypted_lines]
            results.append(f"{block_id}\n" + '\n'.join(decrypted_lines))
        else:
            results.append(f"{block_id}\nNo solution")


    return '\n\n'.join(results)


if __name__ == '__main__':
    filename = 'input_decoder.txt'
    output = decrypt_blocks_from_file(filename)
    print(output)