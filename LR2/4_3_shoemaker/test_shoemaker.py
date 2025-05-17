from shoemaker import solve_shoemaker_problem, parse_input, format_output

def read_test_cases_from_file(filename):
    try:
        with open(filename, 'r') as file:
            input_string = file.read()
        return parse_input(input_string)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

if __name__ == "__main__":
    test_cases = read_test_cases_from_file("C:/PRiTPO/LR2/4_3_shoemaker/shoemaker_tests.txt")
    if test_cases:  # Проверяем, что тесты загружены
        results = solve_shoemaker_problem(test_cases)
        print("Результаты:")
        print(format_output(results))
