"""
Given a rod of length ‘n’, we are asked to cut the rod and sell the
pieces in a way that will maximize the profit. We are also given the price
of every piece of length ‘i’ where ‘1 <= i <= n’.

Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5
"""


def solve_rod_cutting(lengths, prices, rod_length):
	arr_len = len(lengths)
	if arr_len == 0 or rod_length <= 0 or arr_len != len(prices):
		return 0
	
	dp = [[0 for j in range(rod_length + 1)] for i in range(arr_len)]
	
	for i in range(arr_len):
		for c in range(1, rod_length + 1):
			profit1, profit2 = 0, 0
			if lengths[i] <= c:
				profit1 = prices[i] + dp[i][c - lengths[i]]
			if i > 0:
				profit2 = dp[i - 1][c]
			dp[i][c] = max(profit1, profit2)
	return dp[arr_len - 1][rod_length]


print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
