
def sum_of_cubes(a, b):
    total = 0
    for number in range(a, b + 1):
        cube = number * number * number
        total += cube
    return total

if __name__ == "__main__":
    a = int(input("Enter starting number: "))
    b = int(input("Enter ending number: "))
    print("Sum of cubes:", sum_of_cubes(a, b))
