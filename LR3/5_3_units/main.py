def smallest_repunit_length(n):
    """
    Находит длину наименьшего числа, состоящего из единиц, которое кратно n.

    Args:
        n: Целое число (0 < n < 10000), не кратное 2 и 5.

    Returns:
        Длина наименьшего числа, состоящего из единиц, кратного n.
    """

    if n % 2 == 0 or n % 5 == 0:
        raise ValueError("n не должно быть кратно 2 или 5")

    remainder = 1
    length = 1
    while remainder % n != 0:
        remainder = (remainder * 10 + 1) % n
        length += 1
    return length



# Примеры использования:
inputs = [3, 7, 9901]
for n in inputs:
    print(smallest_repunit_length(n))