def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(ch)**2 for ch in str(n))
    return n == 1

if __name__ == "__main__":
    print(is_happy(int(input("Positive integer: "))))
