from collections import Counter

def unique_sum(nums):
    unique = [x for x, count in Counter(nums).items() if count == 1]
    return unique, sum(unique)

if __name__ == "__main__":
    nums = list(map(int, input("Numbers: ").split()))
    items, total = unique_sum(nums)
    print("Unique Elements:", *items if items else ["None"])
    print("Sum:", total)
