def single_number(numbers):
    answer = 0
    for number in numbers:
        answer = answer ^ number
    return answer

if __name__ == "__main__":
    raw = input("Enter integers separated by spaces: ")
    numbers = []
    for item in raw.split():
        numbers.append(int(item))
    print("Single number:", single_number(numbers))
