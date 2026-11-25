def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

if __name__ == "__main__":
    print(hamming_weight(int(input("Positive integer: "))))
