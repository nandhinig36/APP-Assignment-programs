# Q2: Display every palindrome between m and n, inclusive.
def find_palindromes(m, n):
    answers = []
    for number in range(m, n + 1):
        text = str(number)
        if text == text[::-1]:
            answers.append(number)
    return answers

if __name__ == "__main__":
    m = int(input("Enter starting number: "))
    n = int(input("Enter ending number: "))
    print("Palindromes:", find_palindromes(m, n))
