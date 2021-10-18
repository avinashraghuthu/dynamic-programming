def min_del_insert_lcs(input_str1, input_str2):
	lcs_length = find_lcs_length(input_str1, input_str2)
	print("Minimum deletions:", len(input_str1) - lcs_length)
	print("Minimum insertions:", len(input_str2) - lcs_length)

def find_lcs_length(input_str1, input_str2):
	input_str1_len = len(input_str1)
	input_str2_len = len(input_str2)
	dp = [[0 for _ in range(input_str2_len+1)] for _ in range(input_str1_len+1)]
	max_length = 0
	for index1 in range(1, input_str1_len+1):
		for index2 in range(1, input_str2_len+1):
			if input_str1[index1-1] == input_str2[index2-1]:
				dp[index1][index2] = 1 + dp[index1-1][index2-1]
			else:
				dp[index1][index2] = max(dp[index1-1][index2], dp[index1][index2-1])
			max_length = max(max_length, dp[index1][index2])
	return max_length


min_del_insert_lcs("abc", "fbc")
min_del_insert_lcs("abdca", "cbda")
min_del_insert_lcs("passport", "ppsspt")