"""
Given an array of positive numbers, where each element represents the max number
of jumps that can be made forward from that element, write a program to find the
minimum number of jumps needed to reach the end of the array
(starting from the first element). If an element is 0,
then we cannot move through that element.

Input = {2,1,1,1,4}
Output = 3
Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4
"""
#  https://www.geeksforgeeks.org/minimum-number-jumps-reach-endset-2on-solution/

import math


# Method 1: Recursive
def min_jumps_to_end_recursive(arr):
	return min_jumps_to_end_recursive_utils(arr, 0)


def min_jumps_to_end_recursive_utils(arr, current_index):
	arr_len = len(arr)
	if current_index == arr_len - 1:
		return 0
	if arr[current_index] == 0:
		return math.inf
	
	total_jumps = math.inf
	start, end = current_index + 1, current_index + arr[current_index]
	while start < arr_len and start <= end:
		curr_jumps = min_jumps_to_end_recursive_utils(arr, start)
		if curr_jumps != math.inf:
			total_jumps = min(total_jumps, curr_jumps + 1)
		start += 1
	return total_jumps


# Method 2: Bottom Up Approach
def min_jumps_to_end_tabulation(arr):
	arr_len = len(arr)
	
	dp = [math.inf for _ in range(arr_len)]
	dp[0] = 0
	
	for current_index in range(arr_len):
		# for each element in arr find the min steps at each stage
		# if arr[i] val is 3 then current range is (i+1, i+3) ---- step count is +1 wrt current index
		start, end = current_index + 1, current_index + arr[current_index]
		while start < arr_len and start <= end:
			dp[start] = min(dp[start], dp[current_index] + 1)
			start += 1
	return dp[arr_len - 1]


# Method 3 : O(N) optimised
def min_jumps_to_end_optimised(arr):
	arr_len = len(arr)
	
	if arr_len <= 1:
		return 0
	if arr[0] == 0:
		return -1
	
	max_reach = arr[0]
	steps = arr[0]
	jumps = 1
	for i in range(1, arr_len):
		if i == arr_len - 1:
			return jumps
		max_reach = max(max_reach, i + arr[i])
		steps -= 1
		if steps == 0:
			jumps += 1
			
			if i >= max_reach:
				return -1
			
			steps = max_reach - i
	return -1


print(min_jumps_to_end_recursive([2, 1, 1, 1, 4]))
print(min_jumps_to_end_tabulation([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]))
print(min_jumps_to_end_optimised([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]))
