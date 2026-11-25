def move_zeros(nums):
    nonzero = [x for x in nums if x != 0]
    zeros = [x for x in nums if x == 0]
    return nonzero + zeros

if __name__ == "__main__":
    nums = list(map(int, input("Numbers: ").split()))
    print(move_zeros(nums))
