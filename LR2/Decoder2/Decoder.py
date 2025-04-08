def decrypt_blocks_from_file(filename):
    with open(filename, 'r') as file:
        input_data = file.read()
    return decrypt_blocks(input_data)


def decrypt_blocks(input_data):
    known_plain_text = "the quick brown fox jumps over the lazy dog"

    def find_mapping(encrypted_line):
        encrypted_words = encrypted_line.split()
        known_words = known_plain_text.split()

        if len(encrypted_words) != len(known_words):
            return None

        mapping = {}
        for enc_word, known_word in zip(encrypted_words, known_words):
            if len(enc_word) != len(known_word):
                return None
            for enc_char, known_char in zip(enc_word, known_word):
                if enc_char not in mapping:
                    mapping[enc_char] = known_char
                elif mapping[enc_char] != known_char:
                    return None

        if len(set(mapping.values())) != len(mapping):
            return None

        return mapping

    def decrypt_line(line, mapping):
        table = str.maketrans(mapping)
        return line.translate(table)

    blocks = input_data.strip().split('\n\n')
    results = []

    for block in blocks:
        lines = block.strip().split('\n')
        block_id = lines[0]
        encrypted_lines = lines[1:]

        if len(encrypted_lines) > 100 or any(len(line) > 80 for line in encrypted_lines) or \
           any(not line.isascii() or not line.islower() or not all(c.isalpha() or c.isspace() for c in line) for line in
               encrypted_lines):
            results.append(f"{block_id}\nNo solution")
            continue

        found_mapping = None
        for line in encrypted_lines:
            mapping = find_mapping(line)
            if mapping:
                found_mapping = mapping
                break

        if found_mapping:
            decrypted_lines = [decrypt_line(line, found_mapping) for line in encrypted_lines]
            results.append(f"{block_id}\n" + '\n'.join(decrypted_lines))
        else:
            results.append(f"{block_id}\nNo solution")

    return '\n\n'.join(results)

if __name__ == '__main__':
    filename = 'input_decoder.txt' # Или укажите другой файл
    output = decrypt_blocks_from_file(filename)
    print(output)
