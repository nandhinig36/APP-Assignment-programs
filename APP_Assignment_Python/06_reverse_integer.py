def reverse_integer(x):
    sign = -1 if x < 0 else 1
    value = sign * int(str(abs(x))[::-1])
    return value if -(2**31) <= value <= 2**31 - 1 else 0

if __name__ == "__main__":
    print(reverse_integer(int(input("Enter a 32-bit integer: "))))
