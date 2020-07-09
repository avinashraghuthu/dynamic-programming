import math

"""
Given a number array to represent different coin denominations and
a total amount ‘T’, we need to find the minimum number of coins
needed to make change for ‘T’. We can assume an infinite supply of coins,
therefore, each coin can be chosen multiple times.

Denominations: {1,2,3}
Total amount: 5
Output: 2
"""


def min_coin_count(denominations, sum_val):
	arr_len = len(denominations)
	
	if arr_len == 0 or sum_val <= 0:
		return 0
	
	dp = [[math.inf for j in range(sum_val + 1)] for i in range(arr_len)]
	
	for i in range(arr_len):
		dp[i][0] = 0
	
	for i in range(arr_len):
		for s in range(1, sum_val + 1):
			if i > 0:
				dp[i][s] = dp[i - 1][s]
			if denominations[i] <= s:
				dp[i][s] = min(dp[i][s], dp[i][s - denominations[i]] + 1)
	return -1 if dp[arr_len - 1][sum_val] == math.inf else dp[arr_len - 1][sum_val]


print(min_coin_count([1, 2, 3], 5))
print(min_coin_count([1, 2, 3], 11))
print(min_coin_count([1, 2, 3], 7))
print(min_coin_count([3, 5], 7))
