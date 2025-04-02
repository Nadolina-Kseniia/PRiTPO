def minimize_penalty(test_cases):
    results = []

    for orders in test_cases:
        # orders is a list of tuples (Ti, Si)
        indexed_orders = [(Ti, Si, i + 1) for i, (Ti, Si) in enumerate(orders)]

        # Sort by (Si/Ti, index)
        indexed_orders.sort(key=lambda x: (x[1] / x[0], x[2]))

        # Collect the order of indices
        result = [str(order[2]) for order in indexed_orders]
        results.append(" ".join(result))

    return "\n\n".join(results)


def main():
    import sys

    input_data = sys.stdin.read().strip().split("\n")
    test_cases = []
    current_case = []

    for line in input_data:
        if line.strip() == "":
            if current_case:
                test_cases.append(current_case)
                current_case = []
        else:
            if len(current_case) == 0:
                n = int(line.strip())
            else:
                Ti, Si = map(int, line.strip().split())
                current_case.append((Ti, Si))

    if current_case:
        test_cases.append(current_case)

    result = minimize_penalty(test_cases)
    print(result)


if __name__ == "__main__":
    main()