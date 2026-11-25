def is_anagram(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = input("First string: "); t = input("Second string: ")
    print(is_anagram(s, t))
