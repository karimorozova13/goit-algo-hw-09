def find_coins_greedy(coins, total):
    coins.sort(reverse=True)
    cash_folder = {}
    temp = 0
        
    for coin in coins:
        cash_folder[coin] = 0
        while total >= coin:
            total -= coin
            temp += coin
            cash_folder[coin] +=1
    remove_zero_values(cash_folder)
    return cash_folder

def remove_zero_values(dictionary):
    for key in [key for key, value in dictionary.items() if value == 0]:
        del dictionary[key]

def find_min_coins(coins, total):
    coins.sort()
    dp = [float('inf')] * (total + 1)
    coin_counts = {}

    dp[0] = 0

    for coin in coins:
        coin_counts[coin] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_counts[coin] += 1

    # Reconstruct the solution (coin counts)
    result = {}
    remaining_total = total

    for coin in coins:
        result[coin] = coin_counts[coin]
        remaining_total -= coin * coin_counts[coin]

    return result

coins = [50, 25, 10, 5, 2, 1]

print(find_coins_greedy(coins, 113))
print(find_min_coins(coins, 113))

    
