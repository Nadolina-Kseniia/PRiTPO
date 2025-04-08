def solve_shoemaker_problem(test_cases):
    results = []
    for case in test_cases:
        n, jobs = case
        # Sort jobs by the ratio S_i / T_i, higher ratio first, then by lexicographic order on index
        jobs.sort(key=lambda job: (-job[1] / job[0], job[2]))
        # Get the order of job indices
        sequence = [job[2] for job in jobs]
        results.append(sequence)
    return results

def parse_input(input_string):
    lines = input_string.strip().split("\n")
    number_of_cases = int(lines[0].strip())
    test_cases = []
    index = 1
    for _ in range(number_of_cases):
        index += 1  # Skip the blank line
        n = int(lines[index].strip())
        jobs = []
        for i in range(n):
            index += 1
            t, s = map(int, lines[index].strip().split())
            jobs.append((t, s, i + 1))
        test_cases.append((n, jobs))
    return test_cases

def format_output(results):
    output_lines = []
    for result in results:
        output_lines.append(" ".join(map(str, result)))
    return "\n\n".join(output_lines)

# Example usage:
input_data = """
1

4
3 4
1 1000
2 2
5 5
"""

test_cases = parse_input(input_data)
results = solve_shoemaker_problem(test_cases)
output = format_output(results)
print(output)