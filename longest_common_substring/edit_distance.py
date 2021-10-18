def find_min_operations(input_str1, input_str2):
	input_str1_len = len(input_str1)
	input_str2_len = len(input_str2)
	dp = [[-1 for _ in range(input_str2_len+1)] for _ in range(input_str1_len+1)]
	for i in range(input_str1_len+1):
		dp[i][0] = i
	for i in range(input_str2_len+1):
		dp[0][i] = i
	for index1 in range(1, input_str1_len+1):
		for index2 in range(1, input_str2_len+1):
			if input_str1[index1-1] == input_str2[index2-1]:
				dp[index1][index2] = dp[index1-1][index2-1]
			else:
				dp[index1][index2] = 1 + min(dp[index1-1][index2],
											 dp[index1][index2-1],
											 dp[index1-1][index2-1])
	return dp[input_str1_len][input_str2_len]


print(find_min_operations("bat", "but"))
print(find_min_operations("abdca", "cbda"))
print(find_min_operations("passpot", "ppsspqrt"))