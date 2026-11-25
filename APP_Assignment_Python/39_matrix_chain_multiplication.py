def matrix_chain(dimensions):
    matrix_count = len(dimensions) - 1
    cost = [[0 for column in range(matrix_count)] for row in range(matrix_count)]
    split = [[0 for column in range(matrix_count)] for row in range(matrix_count)]

    for chain_length in range(2, matrix_count + 1):
        for start in range(0, matrix_count - chain_length + 1):
            end = start + chain_length - 1
            cost[start][end] = float("inf")
            for middle in range(start, end):
                current_cost = (cost[start][middle] + cost[middle + 1][end]
                                + dimensions[start] * dimensions[middle + 1] * dimensions[end + 1])
                if current_cost < cost[start][end]:
                    cost[start][end] = current_cost
                    split[start][end] = middle

    def parenthesization(start, end):
        if start == end:
            return "A" + str(start + 1)
        middle = split[start][end]
        left = parenthesization(start, middle)
        right = parenthesization(middle + 1, end)
        return "(" + left + " x " + right + ")"

    steps = []
    def make_steps(start, end):
        if start == end:
            return ("A" + str(start + 1), dimensions[start], dimensions[start + 1])
        middle = split[start][end]
        left_name, left_rows, left_cols = make_steps(start, middle)
        right_name, right_rows, right_cols = make_steps(middle + 1, end)
        operation_cost = left_rows * left_cols * right_cols
        result_name = "Result" + str(len(steps) + 1)
        steps.append((left_name, right_name, operation_cost, left_rows, left_cols, right_cols))
        return (result_name, left_rows, right_cols)

    make_steps(0, matrix_count - 1)
    return cost[0][matrix_count - 1], parenthesization(0, matrix_count - 1), steps

if __name__ == "__main__":
    raw = input("Enter dimensions (example: 10 30 5 60): ")
    dimensions = []
    for item in raw.split():
        dimensions.append(int(item))
    minimum_cost, order, steps = matrix_chain(dimensions)
    print("Minimum multiplication cost:", minimum_cost)
    print("Optimal parenthesization:", order)
    print("Multiplication sequence:")
    for number, step in enumerate(steps, 1):
        left, right, operation_cost, rows, common, columns = step
        print("Step", number, ": (", left, "x", right, ") ->", rows, "x", common,
              " multiplied by ", common, "x", columns, "; cost =", operation_cost)
