# Q11: Find the missing number from the range 0 to n.
def missing_number(numbers):
    n = len(numbers)
    expected_total = n * (n + 1) // 2
    actual_total = 0
    for number in numbers:
        actual_total += number
    return expected_total - actual_total

if __name__ == "__main__":
    raw = input("Enter numbers separated by spaces: ")
    numbers = []
    for item in raw.split():
        numbers.append(int(item))
    print("Missing number:", missing_number(numbers))
