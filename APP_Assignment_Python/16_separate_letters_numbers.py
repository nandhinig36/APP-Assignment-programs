def separate(s):
    letters = "".join(ch for ch in s if ch.isalpha())
    digits = "".join(ch for ch in s if ch.isdigit())
    return [letters, digits]

if __name__ == "__main__":
    print(separate(input("Enter string: ")))
