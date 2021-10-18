def find_spm_count(arr, pat_arr):
	arr_len = len(arr)
	pat_arr_len = len(pat_arr)
	if pat_arr_len == 0:
		return 1
	if arr_len == 0 or pat_arr_len > arr_len:
		return 0
	dp = [[0 for _ in range(pat_arr_len+1)] for _ in range(arr_len+1)]
	for i in range(arr_len):
		dp[i][0] = 1
	for arr_index in range(1, arr_len+1):
		for pat_index in range(1, pat_arr_len+1):
			if arr[arr_index-1] == pat_arr[pat_index-1]:
				dp[arr_index][pat_index] = dp[arr_index-1][pat_index-1]
			dp[arr_index][pat_index] += dp[arr_index-1][pat_index]
	return dp[arr_index][pat_index]


print(find_spm_count("baxmx", "ax"))
print(find_spm_count("tomorrow", "tor"))