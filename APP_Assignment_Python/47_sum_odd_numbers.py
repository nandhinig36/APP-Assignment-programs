def sum_odds(values):
    return sum(value for value in values if value % 2 != 0)

def sum_odds_comprehension(values):
    return sum([value for value in values if value % 2 != 0])

def sum_odds_user_function(values):
    return sum_odds(values)

if __name__ == "__main__":
    numbers = list(map(int, input("Numbers: ").split()))
    print("Regular function:", sum_odds(numbers))
    print("List comprehension:", sum_odds_comprehension(numbers))
    print("User-defined function:", sum_odds_user_function(numbers))
