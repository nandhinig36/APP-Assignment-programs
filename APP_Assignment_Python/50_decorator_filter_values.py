from functools import wraps

def filtering_decorator(function):
    @wraps(function)
    def wrapper(values):
        return function(values)
    return wrapper

@filtering_decorator
def remove_greater_than_20(values):
    return list(filter(lambda value: value <= 20, values))

if __name__ == "__main__":
    nums = list(map(int, input("Numbers: ").split()))
    print(remove_greater_than_20(nums))
