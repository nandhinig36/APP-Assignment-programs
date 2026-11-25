def palindromic_substrings(s):
    found = []
    for center in range(2 * len(s) - 1):
        left, right = center // 2, center // 2 + center % 2
        while left >= 0 and right < len(s) and s[left] == s[right]:
            found.append(s[left:right+1])
            left -= 1; right += 1
    return found

if __name__ == "__main__":
    values = palindromic_substrings(input("String: "))
    print("Total Count:", len(values))
    print("Palindromic Substrings:")
    print("\n".join(values))
