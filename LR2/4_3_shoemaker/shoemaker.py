def solve_shoemaker_problem(test_cases):
    results = []
    for case in test_cases:
        if not case:
            continue
        n, jobs = case
        try:
            jobs.sort(key=lambda job: (-job[1] / job[0] if job[0] != 0 else float('-inf'), job[2]))
        except ZeroDivisionError:
            jobs.sort(key=lambda job: (float('-inf'), job[2]))
        sequence = [job[2] for job in jobs]
        results.append(sequence)
    return results


def parse_input(input_string):
    lines = [line.strip() for line in input_string.split("\n") if line.strip()]
    if not lines:
        return []

    try:
        number_of_cases = int(lines[0])
    except (IndexError, ValueError):
        return []

    test_cases = []
    index = 1

    while index < len(lines):
        try:
            n = int(lines[index])
            index += 1
            jobs = []
            for i in range(n):
                if index >= len(lines):
                    break
                parts = lines[index].split()
                if len(parts) != 2:
                    index += 1
                    continue
                t, s = map(int, parts)
                jobs.append((t, s, i + 1))
                index += 1
            test_cases.append((n, jobs))
        except (ValueError, IndexError):
            index += 1
            continue

    return test_cases


def format_output(results):
    output_lines = []
    for result in results:
        output_lines.append(" ".join(map(str, result)))
    return "\n\n".join(output_lines)


def read_test_cases_from_file(filename):
    try:
        with open(filename, 'r') as file:
            input_string = file.read()
        return parse_input(input_string)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {str(e)}")
        return []
