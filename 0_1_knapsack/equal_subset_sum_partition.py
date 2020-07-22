"""
Given a set of positive numbers, find if we can partition it into two
subsets such that the sum of elements in both the subsets is equal.

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
"""


def equal_subset_sum_partition(arr):
	total_sum = sum(arr)
	if total_sum == 0 or total_sum % 2 != 0:
		return False
	subset_sum = total_sum // 2
	arr_len = len(arr)
	dp = [[False for j in range(subset_sum + 1)] for i in range(arr_len)]
	
	for i in range(arr_len):
		dp[i][0] = True
	
	for s in range(subset_sum + 1):
		if arr[0] == s:
			dp[0][s] = True
	
	for i in range(1, arr_len):
		for s in range(1, subset_sum + 1):
			if dp[i - 1][s]:
				dp[i][s] = dp[i - 1][s]
			elif arr[i] <= s:
				dp[i][s] = dp[i - 1][s - arr[i]]
	return dp[arr_len - 1][subset_sum]


print("Can partition: " + str(equal_subset_sum_partition([1, 2, 3, 4])))
print("Can partition: " + str(equal_subset_sum_partition([1, 1, 3, 4, 7])))
print("Can partition: " + str(equal_subset_sum_partition([2, 3, 4, 6])))
