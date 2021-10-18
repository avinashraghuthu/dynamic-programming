def find_las_length(arr):
	arr_len = len(arr)
	dp = [[1 for _ in range(2)] for _ in range(arr_len)]
	max_length = 0
	for current_index in range(1, arr_len):
		for previous_index in range(current_index):
			if arr[current_index] > arr[previous_index]:
				dp[current_index][0] = max(dp[current_index][0], 1 + dp[previous_index][1])
				max_length = max(max_length, dp[current_index][0])
			elif arr[current_index] < arr[previous_index]:
				dp[current_index][1] = max(dp[current_index][1], 1 + dp[previous_index][0])
				max_length = max(max_length, dp[current_index][1])
	return max_length


print(find_las_length([1, 2, 3, 4]))
print(find_las_length([3, 2, 1, 4]))
print(find_las_length([1, 3, 2, 4]))