def find_min_del(arr):
	return len(arr) - find_lis_length(arr)


def find_lis_length(arr):
	arr_len = len(arr)
	dp = [1 for _ in range(arr_len)]
	max_length = 1
	for current_index in range(1, arr_len):
		for previous_index in range(current_index):
			if arr[current_index] > arr[previous_index] and \
				dp[current_index] <= dp[previous_index]:
				dp[current_index] = 1 + dp[previous_index]
				max_length = max(max_length, dp[current_index])
	return max_length


print(find_min_del([4, 2, 3, 6, 10, 1, 12]))
print(find_min_del([-4, 10, 3, 7, 15]))
print(find_min_del([3, 2, 1, 0]))