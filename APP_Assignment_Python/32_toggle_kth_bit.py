def toggle_kth_bit(n, k):
    if k < 0: raise ValueError("k must be non-negative (0-based)")
    return n ^ (1 << k)

if __name__ == "__main__":
    n, k = map(int, input("Enter n and zero-based k: ").split())
    print(toggle_kth_bit(n, k))
