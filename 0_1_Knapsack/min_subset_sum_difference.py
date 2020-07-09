"""
Given a set of positive numbers, partition the set into two subsets with
a minimum difference between their subset sums.

Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
"""


def min_subset_sum_partition(arr):
	total_sum = sum(arr)
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
	sum1 = 0
	for i in range(subset_sum, -1, -1):
		if dp[arr_len - 1][i]:
			sum1 = i
			break
	sum2 = total_sum - sum1
	return abs(sum1 - sum2)


print("Can partition: " + str(min_subset_sum_partition([1, 2, 3, 9])))
print("Can partition: " + str(min_subset_sum_partition([1, 2, 7, 1, 5])))
print("Can partition: " + str(min_subset_sum_partition([1, 3, 100, 4])))
