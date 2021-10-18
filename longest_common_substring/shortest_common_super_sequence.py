def find_scss_length(arr1, arr2):
	arr1_len = len(arr1)
	arr2_len = len(arr2)
	dp = [[0 for _ in range(arr2_len+1)] for _ in range(arr1_len+1)]
	for i in range(arr1_len+1):
		dp[i][0] = i
	for i in range(arr2_len+1):
		dp[0][i] = i
	for index1 in range(1, arr1_len+1):
		for index2 in range(1, arr2_len+1):
			if arr1[index1-1] == arr2[index2-1]:
				dp[index1][index2] = 1 + dp[index1-1][index2-1]
			else:
				dp[index1][index2] = 1 + min(dp[index1-1][index2], dp[index1][index2-1])
	return dp[arr1_len][arr2_len]


print(find_scss_length("abcf", "bdcf"))
print(find_scss_length("dynamic", "programming"))