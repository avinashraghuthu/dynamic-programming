"""
Given an infinite supply of ‘n’ coin denominations and a total money amount,
we are asked to find the total number of distinct ways to make up that amount.

Denominations: {1,2,3}
Total amount: 5
Output: 5
"""


# maximum no of ways we can get that sum_val
def coin_change(denominations, sum_val):
	arr_len = len(denominations)
	if arr_len == 0 or sum_val < 0:
		return 0
	dp = [[0 for j in range(sum_val + 1)] for i in range(arr_len)]
	
	for i in range(arr_len):
		dp[i][0] = 1
	
	for i in range(arr_len):
		for s in range(1, sum_val + 1):
			if i > 0:
				dp[i][s] = dp[i - 1][s]
			if denominations[i] <= s:
				dp[i][s] += dp[i][s - denominations[i]]
	return dp[arr_len - 1][sum_val]


print(coin_change([1, 2, 3], 5))
