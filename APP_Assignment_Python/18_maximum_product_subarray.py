def max_product(nums):
    high = low = answer = nums[0]
    for value in nums[1:]:
        if value < 0: high, low = low, high
        high = max(value, high * value)
        low = min(value, low * value)
        answer = max(answer, high)
    return answer

if __name__ == "__main__":
    nums = list(map(int, input("Numbers: ").split()))
    print(max_product(nums))
