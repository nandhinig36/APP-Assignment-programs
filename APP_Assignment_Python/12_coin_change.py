def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value: dp[value] = min(dp[value], dp[value-coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1

if __name__ == "__main__":
    coins = list(map(int, input("Coin denominations: ").split()))
    amount = int(input("Amount: "))
    print("Minimum coins:", coin_change(coins, amount))
