def find_lbs_length(arr):
	arr_len = len(arr)
	lis_dp = [1 for _ in range(arr_len)]
	
	# LIS from left to right
	for current_index in range(1, arr_len):
		for previous_index in range(current_index):
			if arr[current_index] > arr[previous_index] and \
					lis_dp[current_index] <= lis_dp[previous_index]:
				lis_dp[current_index] = 1 + lis_dp[previous_index]
	rev_lis_dp = [1 for _ in range(arr_len)]
	
	# Reverse LIS from right to left
	for current_index in range(arr_len - 1, -1, -1):
		for next_index in range(current_index + 1, arr_len):
			if arr[current_index] > arr[next_index] and \
					rev_lis_dp[current_index] <= rev_lis_dp[next_index]:
				rev_lis_dp[current_index] = 1 + rev_lis_dp[next_index]
	max_length = 0
	for i in range(arr_len):
		max_length = max(max_length, lis_dp[i] + rev_lis_dp[i] - 1)
	return max_length


print(find_lbs_length([4, 2, 3, 6, 10, 1, 12]))
print(find_lbs_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))
