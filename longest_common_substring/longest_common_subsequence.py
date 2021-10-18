def find_lcs_length_recursion(input_str1, input_str2):
	return find_lcs_length_recursion_utils(input_str1, input_str2, 0, 0)


def find_lcs_length_recursion_utils(input_str1, input_str2, index1, index2):
	if index1 == len(input_str1) or index2 == len(input_str2):
		return 0
	
	if input_str1[index1] == input_str2[index2]:
		return 1 + find_lcs_length_recursion_utils(input_str1, input_str2, index1+1, index2+1)
	
	count1 = find_lcs_length_recursion_utils(input_str1, input_str2, index1+1, index2)
	count2 = find_lcs_length_recursion_utils(input_str1, input_str2, index1, index2+1)
	return max(count1, count2)


def find_lcs_length_dp(input_str1, input_str2):
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
	

print(find_lcs_length_dp("abdca", "cbda"))
print(find_lcs_length_dp("passport", "ppsspt"))
