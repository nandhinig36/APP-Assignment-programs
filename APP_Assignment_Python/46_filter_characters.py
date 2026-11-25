def filter_characters(text, unwanted):
    return "".join(ch for ch in text if ch not in set(unwanted))

if __name__ == "__main__":
    text = input("Original string: ")
    unwanted = input("Characters to remove: ")
    print(filter_characters(text, unwanted))
