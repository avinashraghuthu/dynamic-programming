def max_sum_lis(arr):
	arr_len = len(arr)
	dp = [0 for _ in range(arr_len)]
	
	for i in range(arr_len):
		dp[i] = arr[i]
	
	max_sum = 0
	for current_index in range(1, arr_len):
		for previous_index in range(current_index):
			if arr[current_index] > arr[previous_index] and \
				dp[current_index] < dp[previous_index] + arr[current_index]:
				dp[current_index] = arr[current_index] + dp[previous_index]
				max_sum = max(max_sum, dp[current_index])
	return max_sum


print(max_sum_lis([4, 1, 2, 6, 10, 1, 12]))
print(max_sum_lis([-4, 10, 3, 7, 15]))