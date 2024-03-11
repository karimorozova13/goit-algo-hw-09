import timeit
import json

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
    dp = [[float('inf')]*(total + 1) for _ in range(len(coins) + 1)]
    dp[0][0] = 0

    for i in range(1, len(coins) + 1):
        for w in range(total + 1):
            if coins[i - 1] <= w:
                dp[i][w] = min(dp[i - 1][w], 1 + dp[i][w - coins[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    coin_counts = {}
    i, w = len(coins), total
    
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            if coins[i - 1] in coin_counts:
                coin_counts[coins[i - 1]] += 1
            else:
                coin_counts[coins[i - 1]] = 1
            w -= coins[i - 1]
        else:
            i -= 1
    sorted_coin_counts = dict(sorted(coin_counts.items(), key=lambda x: x[0]))
    return sorted_coin_counts


coins = [50, 25, 10, 5, 2, 1]

total_min = 113
total_medium = 725
total_max = 9999

greedy_res_min = json.dumps(find_coins_greedy(coins, total_min))
dp_res_min = json.dumps(find_min_coins(coins, total_min))
greedy_res_medium = json.dumps(find_coins_greedy(coins, total_medium))
dp_res_medium = json.dumps(find_min_coins(coins, total_medium))
greedy_res_max = json.dumps(find_coins_greedy(coins, total_max))
dp_res_max = json.dumps(find_min_coins(coins, total_max))

time_taken_greedy_min = timeit.timeit(lambda: find_coins_greedy(coins, total_min), number=3)
time_taken_dp_min = timeit.timeit(lambda: find_min_coins(coins, total_min), number=3)
time_taken_greedy_medium = timeit.timeit(lambda: find_coins_greedy(coins, total_medium), number=3)
time_taken_dp_medium = timeit.timeit(lambda: find_min_coins(coins, total_medium), number=3)
time_taken_greedy_max = timeit.timeit(lambda: find_coins_greedy(coins, total_max), number=3)
time_taken_dp_max = timeit.timeit(lambda: find_min_coins(coins, total_max), number=3)


print(f"| {'Algorithm':<40} | {'Result':<40} | {'Time taken':<20} | {'Is it faster':<20} |")
print(f"| {'-'*40} | {'-'*40} | {'-'*20} | {'-'*20} |")
print(f"| {'Greedy allornathiers min amount':<40} | {greedy_res_min:<40} | {time_taken_greedy_min:20.5f} | {time_taken_greedy_min < time_taken_dp_min:>20} |")
print(f"| {'Dynamic programming min amount':<40} | {dp_res_min:<40} | {time_taken_dp_min:20.5f} | {time_taken_greedy_min > time_taken_dp_min:>20} |")
print(f"| {'-'*40} | {'-'*40} | {'-'*20} | {'-'*20} |")
print(f"| {'Greedy allornathiers medium amount':<40} | {greedy_res_medium:<40} | {time_taken_greedy_medium:20.5f} | {time_taken_greedy_medium < time_taken_dp_medium:>20} |")
print(f"| {'Dynamic programming medium amount':<40} | {dp_res_medium:<40} | {time_taken_dp_medium:20.5f} | {time_taken_greedy_medium > time_taken_dp_medium:>20} |")
print(f"| {'-'*40} | {'-'*40} | {'-'*20} | {'-'*20} |")
print(f"| {'Greedy allornathiers max amount':<40} | {greedy_res_max:<40} | {time_taken_greedy_max:20.5f} | {time_taken_greedy_max < time_taken_dp_max:>20} |")
print(f"| {'Dynamic programming max amount':<40} | {dp_res_max:<40} | {time_taken_dp_max:20.5f} | {time_taken_greedy_max > time_taken_dp_max:>20} |")


    
