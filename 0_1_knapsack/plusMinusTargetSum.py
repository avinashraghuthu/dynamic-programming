"""
Given a set of positive numbers (non zero) and a target sum ‘S’.
Each number should be assigned either a ‘+’ or ‘-’ sign.
We need to find out total ways to assign symbols to make the sum of
numbers equal to target ‘S’.

Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3}
			& {-1+1-2+3} & {+1+1+2-3}
"""


def plusMinusTargetSum(arr, sum_val):
	total_sum = sum(arr)
	if total_sum < sum_val or (total_sum + sum_val) % 2 != 0:
		return 0
	required_subset_sum = (total_sum + sum_val) // 2
	return subset_sum_count(arr, required_subset_sum)


def subset_sum_count(arr, sum_val):
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


print("Total ways: " + str(plusMinusTargetSum([1, 1, 2, 3], 1)))
print("Total ways: " + str(plusMinusTargetSum([1, 2, 7, 1], 9)))
