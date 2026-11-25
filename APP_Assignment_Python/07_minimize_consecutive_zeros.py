from itertools import combinations

def solve(length, ones):
    if not 0 <= ones <= length: raise ValueError("Require 0 <= K <= L")
    results = []
    for positions in combinations(range(length), ones):
        selected = set(positions)
        bits = "".join("1" if i in selected else "0" for i in range(length))
        longest = max(map(len, bits.split("1")), default=0)
        results.append((bits, longest))
    best = min((zeros for _, zeros in results), default=0)
    return results, [bits for bits, zeros in results if zeros == best], best

if __name__ == "__main__":
    L, K = map(int, input("Enter L K: ").split())
    rows, optimal, best = solve(L, K)
    print("Possible Strings:")
    for bits, zeros in rows: print(f"{bits} -> max zeros = {zeros}")
    print("Optimal Arrangement(s):", ", ".join(optimal))
    print("Minimum Longest Zero Block:", best)
