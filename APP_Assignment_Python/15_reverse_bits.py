def reverse_bits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

if __name__ == "__main__":
    print(reverse_bits(int(input("Enter integer: "))))
