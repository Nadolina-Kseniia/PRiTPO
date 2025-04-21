def decrypt_texts(cases):
    # The plaintext we're matching against
    plain_text = "the quick brown fox jumps over the lazy dog"

    results = []

    for case in cases:
        solution_found = False
        decryption_mapping = {}
        case_result = []

        for line in case:
            if len(line) == len(plain_text):
                # Try to map each letter from the encrypted line to the plain_text
                temp_mapping = {}
                valid = True
                for c1, c2 in zip(line, plain_text):
                    if c1 in temp_mapping:
                        if temp_mapping[c1] != c2:
                            valid = False
                            break
                    else:
                        temp_mapping[c1] = c2

                # Ensure that the mapping is one-to-one
                if valid and len(set(temp_mapping.values())) == len(temp_mapping.values()):
                    decryption_mapping = temp_mapping
                    solution_found = True
                    break

        if solution_found:
            for line in case:
                translated = "".join(decryption_mapping.get(char, char) for char in line)
                case_result.append(translated)
        else:
            case_result.append("No solution.")

        results.append(case_result)

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    num_cases = int(data[0].strip())

    index = 0
    cases = []

    for _ in range(num_cases):
        case = []
        #index += 1  # Skip the blank line
        while index < len(data) and data[index].strip():
            case.append(data[index].strip())
            index += 1
        cases.append(case)

    results = decrypt_texts(cases)

    for i, result in enumerate(results):
        if i > 0:
            print()  # Blank line between each test case

        for line in result:
            print(line)

if __name__ == '__main__':
    main()
# закончить ввод ctrl+D