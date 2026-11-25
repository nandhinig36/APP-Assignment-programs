def climb(n):
    patterns = []
    def build(remaining, path):
        if remaining == 0:
            patterns.append(path); return
        if remaining >= 1: build(remaining-1, path+[1])
        if remaining >= 2: build(remaining-2, path+[2])
    build(n, [])
    return patterns

if __name__ == "__main__":
    n = int(input("Number of stairs: "))
    ways = climb(n)
    print("Total distinct ways:", len(ways))
    for pattern in ways: print(pattern)
