import pytest
from count_numbers import count_numbers

test_cases = [
    (0, 1),    # только пустая строка
    (1, 2),    # "1" или "4"
    (2, 5),    # 11, 14, 41, 44, 2
    (3, 13),   # 111(8), 12(2), 21(2), 3(1) → 8+2+2+1=13
    (5, 84),
    (10, 9003)
]

@pytest.mark.parametrize("n, expected", test_cases)
def test_count_numbers(n, expected):
    assert count_numbers(n) == expected

def test_main(monkeypatch, capsys):
    from count_numbers import main
    import io
    monkeypatch.setattr('sys.stdin', io.StringIO("2\n3\n"))
    main()
    captured = capsys.readouterr()
    assert captured.out == "5\n13\n"
