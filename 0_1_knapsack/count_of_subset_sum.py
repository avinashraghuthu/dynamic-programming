"""
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
"""


def count_subset_sum(arr, sum_val):
	arr_len = len(arr)
	
	dp = [[0 for j in range(sum_val + 1)] for i in range(arr_len)]
	
	for i in range(arr_len):
		dp[i][0] = 1
	
	for s in range(sum_val + 1):
		if arr[0] == s:
			dp[0][s] = 1
	
	for i in range(1, arr_len):
		for s in range(1, sum_val + 1):
			dp[i][s] = dp[i - 1][s]
			if arr[i] <= s:
				dp[i][s] += dp[i - 1][s - arr[i]]
	return dp[arr_len - 1][sum_val]


print("Total number of subsets " + str(count_subset_sum([1, 1, 2, 3], 124)))
print("Total number of subsets: " + str(count_subset_sum([1, 2, 7, 1, 5], 9)))
