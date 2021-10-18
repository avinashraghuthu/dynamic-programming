def find_lrs_length(arr):
	arr_len = len(arr)
	dp = [[0 for _ in range(arr_len+1)] for _ in range(arr_len+1)]
	max_length = 0
	for index1 in range(1, arr_len+1):
		for index2 in range(1, arr_len+1):
			if index1 != index2 and arr[index1-1] ==  arr[index2-1]:
				dp[index1][index2] = 1 + dp[index1-1][index2-1]
			else:
				dp[index1][index2] = max(dp[index1-1][index2], dp[index1][index2-1])
			max_length = max(max_length, dp[index1][index2])
	return max_length


print(find_lrs_length("tomorrow"))
print(find_lrs_length("aabdbcec"))
print(find_lrs_length("fmff"))