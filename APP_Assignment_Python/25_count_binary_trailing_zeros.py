def trailing_zeros(n):
    if n <= 0: raise ValueError("n must be positive")
    return (n & -n).bit_length() - 1

if __name__ == "__main__":
    print(trailing_zeros(int(input("Positive integer: "))))
