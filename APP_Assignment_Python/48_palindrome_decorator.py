from functools import wraps

def palindrome_check(function):
    @wraps(function)
    def wrapper(value):
        result = function(value)
        print("Palindrome:" if result else "Not a palindrome")
        return result
    return wrapper

@palindrome_check
def is_palindrome_number(number):
    text = str(number)
    return text == text[::-1]

if __name__ == "__main__":
    is_palindrome_number(input("Enter a number: ").strip())
