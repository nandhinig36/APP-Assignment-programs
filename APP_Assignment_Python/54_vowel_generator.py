def getvowels(name):
    vowels = "aeiouAEIOU"
    for character in name:
        if character in vowels:
            yield character

if __name__ == "__main__":
    # Nandhini is a sample input; the user can enter any name.
    name = input("Enter name [example: Nandhini]: ")
    print("Vowels in the name:")
    for vowel in getvowels(name):
        print(vowel)
