"""
Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
"""


def subset_sum(arr, sum_val):
	arr_len = len(arr)
	
	dp = [[False for j in range(sum_val + 1)] for i in range(arr_len)]
	
	for i in range(arr_len):
		dp[i][0] = True
	
	for s in range(sum_val + 1):
		if arr[0] == s:
			dp[0][s] = True
	
	for i in range(1, arr_len):
		for s in range(1, sum_val + 1):
			if dp[i - 1][s]:
				dp[i][s] = dp[i - 1][s]
			elif arr[i] <= s:
				dp[i][s] = dp[i - 1][s - arr[i]]
	return dp[arr_len - 1][sum_val]


print("Can partition: " + str(subset_sum([1, 2, 3, 7], 6)))
print("Can partition: " + str(subset_sum([1, 2, 7, 1, 5], 10)))
print("Can partition: " + str(subset_sum([1, 3, 4, 8], 6)))
