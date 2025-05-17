import pytest
from Decoder import decrypt_texts


def test_decrypt_texts():
    test_cases = [
        {
            "input": ["gsv jfrxp ybgsrh", "nfyb qnweql"],
            "expected": ["the quick brown", "fox jumps"]
        },
        {
            "input": ["gsv xlwv rm", "nfgzi"],
            "expected": ["the lazy dog", "quick"]
        },
        {
            "input": ["zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmno"],
            "expected": ["the quick brown fox jumps", "over the lazy dog"]
        },
        {
            "input": ["abcdefgh", "ijklmnop", "qrstuvwxyz"],
            "expected": ["No solution."]
        },
        {
            "input": ["the quick brown fox jumps over the lazy dog"],
            "expected": ["the quick brown fox jumps over the lazy dog"]
        }
    ]

    for test in test_cases:
        result = decrypt_texts([test["input"]])
        assert result[0] == test["expected"], f"Test failed for input: {test['input']}"


def test_decrypt_texts_from_file():
    with open("test_data.txt", "r") as f:
        lines = f.read().splitlines()

    num_cases = int(lines[0])
    cases = []
    index = 1

    for _ in range(num_cases):
        case = []
        while index < len(lines) and lines[index].strip() == "":
            index += 1
        while index < len(lines) and lines[index].strip() != "":
            case.append(lines[index].strip())
            index += 1
        cases.append(case)

    results = decrypt_texts(cases)

    expected_results = [
        ["the quick brown", "fox jumps"],
        ["the lazy dog", "quick"],
        ["No solution."]
    ]

    for i, (result, expected) in enumerate(zip(results, expected_results)):
        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"


if __name__ == "__main__":
    pytest.main()
