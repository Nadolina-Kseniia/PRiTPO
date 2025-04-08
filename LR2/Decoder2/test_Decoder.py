import unittest
from Decoder import decrypt_blocks_from_file, decrypt_blocks

class TestDecoder(unittest.TestCase):

    def test_decrypt_blocks_simple(self):
        with open("test_input_simple.txt", "r") as f_in, open("test_output_simple.txt", "r") as f_out:
            input_data = f_in.read()
            expected_output = f_out.read()
        self.assertEqual(decrypt_blocks(input_data), expected_output)

    def test_decrypt_blocks_no_solution(self):
        with open("test_input_no_solution.txt", "r") as f:
            input_data = f.read()
        expected_output = "2\nNo solution"
        self.assertEqual(decrypt_blocks(input_data), expected_output)

    # Добавьте другие тесты по аналогии

if __name__ == '__main__':
    unittest.main()
