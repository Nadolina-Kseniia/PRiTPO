# test_Decoder.py

import pytest
from Decoder import decrypt_texts

def test_decrypt_texts():
    test_cases = [
        {
            "input": [
                "gsv jfrxp ybgsrh",
                "nfyb qnweql"
            ],
            "expected": [
                "the quick brown",
                "fox jumps",
            ]
        },
        {
            "input": [
                "gsv xlwv rm",
                "nfgzi"
            ],
            "expected": [
                "the lazy dog",
                "quick",
            ]
        },
        {
            "input": [
                "zyxwvutsrqponmlkjihgfedcba",
                "abcdefghijklmno"
            ],
            "expected": [
                "the quick brown fox jumps",
                "over the lazy dog"
            ]
        },
        {
            "input": [
                "abcdefgh",
                "ijklmnop",
                "qrstuvwxyz"
            ],
            "expected": [
                "No solution."
            ]
        },
        {
            "input": [
                "the quick brown fox jumps over the lazy dog"
            ],
            "expected": [
                "the quick brown fox jumps over the lazy dog"
            ]
        }
    ]

    for test in test_cases:
        result = decrypt_texts([test["input"]])
        assert result[0] == test["expected"], f"Test failed for input: {test['input']}"

if __name__ == "__main__":
    pytest.main()
