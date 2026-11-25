def longest_unique_substring(s):
    last_seen = [-1] * 26
    left = best = 0
    for right, ch in enumerate(s):
        index = ord(ch)-ord("a")
        left = max(left, last_seen[index]+1)
        last_seen[index] = right
        best = max(best, right-left+1)
    return best

if __name__ == "__main__":
    print(longest_unique_substring(input("Lowercase string: ")))
