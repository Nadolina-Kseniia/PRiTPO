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

        # Попытка найти маппинг через перебор
        mapping = {}
        used_plain_letters = set()
        used_cipher_letters = set()

        def backtrack(i, temp_map, used_plain):
            if i == len(cipher_words):
                return temp_map

            cipher_word = cipher_words[i]
            length = len(cipher_word)

            for plain_word in known_by_length.get(length, []):
                if plain_word in used_plain:
                    continue

                temp = {}
                valid = True
                for c, p in zip(cipher_word, plain_word):
                    if c in temp_map:
                        if temp_map[c] != p:
                            valid = False
                            break
                    else:
                        if p in used_plain_letters:
                            valid = False
                            break
                        temp[c] = p

                if valid:
                    for c, p in zip(cipher_word, plain_word):
                        temp_map[c] = p
                        used_plain_letters.add(p)
                        used_cipher_letters.add(c)
                    used_plain.add(plain_word)
                    result = backtrack(i + 1, temp_map, used_plain)
                    if result:
                        return result
                    used_plain.remove(plain_word)
                    for c in cipher_word:
                        p = temp_map.pop(c)
                        used_plain_letters.remove(p)
                        used_cipher_letters.remove(c)
            return None

        mapping = backtrack(0, {}, set())
        if not mapping:
            results.append(["No solution."])
            continue

        decrypted_case = []
        for line in current_case:
            decrypted_line = []
            for char in line:
                if char == ' ':
                    decrypted_line.append(' ')
                elif char in mapping:
                    decrypted_line.append(mapping[char])
                else:
                    decrypted_case = ["No solution."]
                    break
            if decrypted_case:
                break
            decrypted_case.append(''.join(decrypted_line))
        results.append(decrypted_case if decrypted_case else ["No solution."])

    return results