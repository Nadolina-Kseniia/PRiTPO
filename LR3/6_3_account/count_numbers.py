def count_numbers(n):
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    # digits: 1 (может быть 1 или 4), 2, 3
    for i in range(1, n + 1):
        # Для цифры 1 (2 варианта)
        if i >= 1:
            dp[i] += 2 * dp[i - 1]
        # Для цифры 2
        if i >= 2:
            dp[i] += dp[i - 2]
        # Для цифры 3
        if i >= 3:
            dp[i] += dp[i - 3]
    return dp[n]

def main():
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        print(count_numbers(n))

if __name__ == "__main__":
    main()
