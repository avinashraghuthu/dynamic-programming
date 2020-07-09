import math

"""
Given a number array to represent possible ribbon lengths and a
total ribbon length ‘n’, we need to find the maximum number
of pieces that the ribbon can be cut into.
n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.
"""


def max_ribbon_cut_count(ribbon_lengths, total_ribbon_length):
	arr_len = len(ribbon_lengths)
	if arr_len == 0 or total_ribbon_length <= 0:
		return 0
	
	dp = [[-math.inf for j in range(total_ribbon_length + 1)] for i in range(arr_len)]
	
	for i in range(arr_len):
		dp[i][0] = 0
	
	for i in range(arr_len):
		for s in range(1, total_ribbon_length + 1):
			if i > 0:
				dp[i][s] = dp[i - 1][s]
			if ribbon_lengths[i] <= s:
				dp[i][s] = max(dp[i - 1][s], 1 + dp[i][s - ribbon_lengths[i]])
	return -1 if dp[arr_len - 1][total_ribbon_length] == -math.inf else \
		dp[arr_len - 1][total_ribbon_length]


print(max_ribbon_cut_count([2, 3, 5], 5))
print(max_ribbon_cut_count([2, 3], 7))
print(max_ribbon_cut_count([3, 5, 7], 13))
print(max_ribbon_cut_count([3, 5], 7))
