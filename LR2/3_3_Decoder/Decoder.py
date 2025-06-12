def decrypt_texts(cases):
    known_words = set("the quick brown fox jumps over the lazy dog".split())
    known_by_length = {}
    for word in known_words:
        known_by_length.setdefault(len(word), []).append(word)

    results = []

    for current_case in cases:
        cipher_words = []
        for line in current_case:
            cipher_words.extend(line.split())

        mapping = None

        def backtrack(i, temp_map, used_plain, used_plain_letters, used_cipher_letters):
            if i == len(cipher_words):
                return temp_map
            cipher_word = cipher_words[i]
            length = len(cipher_word)
            for plain_word in known_by_length.get(length, []):
                if plain_word in used_plain:
                    continue
                new_temp_map = temp_map.copy()
                new_used_plain = used_plain.copy()
                new_used_plain_letters = used_plain_letters.copy()
                new_used_cipher_letters = used_cipher_letters.copy()
                valid = True
                for c, p in zip(cipher_word, plain_word):
                    if c in new_temp_map:
                        if new_temp_map[c] != p:
                            valid = False
                            break
                    else:
                        if p in new_used_plain_letters or c in new_used_cipher_letters:
                            valid = False
                            break
                        new_temp_map[c] = p
                        new_used_plain_letters.add(p)
                        new_used_cipher_letters.add(c)
                if valid:
                    new_used_plain.add(plain_word)
                    result = backtrack(i + 1, new_temp_map, new_used_plain, new_used_plain_letters, new_used_cipher_letters)
                    if result is not None:
                        return result
            return None

        mapping = backtrack(0, {}, set(), set(), set())
        if not mapping:
            results.append(["No solution."])
            continue

        decrypted_case = []
        has_error = False
        for line in current_case:
            decrypted_line = []
            for char in line:
                if char == ' ':
                    decrypted_line.append(' ')
                elif char in mapping:
                    decrypted_line.append(mapping[char])
                else:
                    decrypted_case = ["No solution."]
                    has_error = True
                    break
            if has_error:
                break
            decrypted_case.append(''.join(decrypted_line))
        if has_error:
            results.append(["No solution."])
        else:
            results.append(decrypted_case)

    return results