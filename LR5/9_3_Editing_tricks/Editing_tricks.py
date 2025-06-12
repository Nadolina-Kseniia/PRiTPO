def is_edit_step(word1, word2):
    """Проверяет, можно ли преобразовать word1 в word2 за один шаг редактирования."""
    len1 = len(word1)
    len2 = len(word2)
    diff = abs(len1 - len2)

    if diff > 1:
        return False

    if diff == 0:    # Замена буквы
        changes = 0
        for i in range(len1):
            if word1[i] != word2[i]:
                changes += 1
        return changes == 1

    elif len1 > len2:   # Удаление буквы
        for i in range(len1):
            if word1[:i] + word1[i + 1:] == word2:
                return True
        return False
    else:    # Добавление буквы
        for i in range(len2):
            if word2[:i] + word2[i + 1:] == word1:
                return True
        return False


def longest_edit_step_ladder(lexigraf):
    """Вычисляет длину наибольшей лесенки редактирования."""
    n = len(lexigraf)
    dp = [1] * n     # dp[i] хранит длину наибольшей лесенки, заканчивающейся на dictionary[i]

    for i in range(1, n):
        for j in range(i):
            if is_edit_step(lexigraf[j], lexigraf[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Словарь уже вписан здесь
dictionary = ["cat", "dig", "dog", "fig", "fin", "fine", "fog", "log", "wine"]


# Вычисление и вывод результата
result = longest_edit_step_ladder(dictionary)
print(result)
