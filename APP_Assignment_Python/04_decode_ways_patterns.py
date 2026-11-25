def decode(s):
    results = []
    def backtrack(i, path):
        if i == len(s):
            results.append("".join(path))
            return
        if s[i] == "0":
            return
        backtrack(i + 1, path + [chr(64 + int(s[i]))])
        if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
            backtrack(i + 2, path + [chr(64 + int(s[i:i+2]))])
    backtrack(0, [])
    return results

if __name__ == "__main__":
    s = input("Digit string: ").strip()
    ways = decode(s)
    print("Total Ways:", len(ways))
    print("Decoded Strings:")
    print("\n".join(ways) if ways else "None")
