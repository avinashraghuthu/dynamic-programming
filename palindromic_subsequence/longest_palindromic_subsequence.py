"""
Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
In a palindromic subsequence, elements read the same backward and forward.

Example 1:

Input: "abdbca"
Output: 5
Explanation: LPS is "abdba".
"""


def find_lps_length_recursion(input_str):
	return find_lps_length_recursion_utils(input_str, 0, len(input_str) - 1)


def find_lps_length_recursion_utils(input_str, start_index, end_index):
	if start_index > end_index:
		return 0
	
	if start_index == end_index:
		return 1
	
	if input_str[start_index] == input_str[end_index]:
		return 2 + find_lps_length_recursion_utils(input_str,
												   start_index + 1,
												   end_index - 1)
	start_index_ignore_count = find_lps_length_recursion_utils(input_str,
															   start_index + 1,
															   end_index)
	end_index_ignore_count = find_lps_length_recursion_utils(input_str,
															 start_index,
															 end_index - 1)
	return max(start_index_ignore_count, end_index_ignore_count)


def find_lps_length_memoization(input_str):
	input_str_len = len(input_str)
	dp = [[-1 for _ in range(input_str_len)] for _ in range(input_str_len)]
	return find_lps_length_memoization_utils(input_str, dp, 0, input_str_len - 1)


def find_lps_length_memoization_utils(input_str, dp, start_index, end_index):
	if start_index > end_index:
		return 0
	
	if start_index == end_index:
		return 1
	
	if dp[start_index][end_index] == -1:
		if input_str[start_index] == input_str[end_index]:
			dp[start_index][end_index] = 2 + find_lps_length_memoization_utils(input_str,
																			   dp, start_index + 1, end_index - 1)
		else:
			start_index_ignore_count = find_lps_length_memoization_utils(input_str,
																		 dp, start_index + 1, end_index)
			end_index_ignore_count = find_lps_length_memoization_utils(input_str,
																	   dp, start_index, end_index - 1)
			dp[start_index][end_index] = max(start_index_ignore_count, end_index_ignore_count)
	return dp[start_index][end_index]


def find_lps_length_tabulation(input_str):
	input_str_len = len(input_str)
	dp = [[0 for _ in range(input_str_len)] for _ in range(input_str_len)]
	for i in range(input_str_len):
		dp[i][i] = 1
	
	for start_index in range(input_str_len - 1, -1, -1):
		for end_index in range(start_index + 1, input_str_len):
			if input_str[start_index] == input_str[end_index]:
				dp[start_index][end_index] = 2 + dp[start_index + 1][end_index - 1]
			else:
				dp[start_index][end_index] = max(dp[start_index + 1][end_index],
												 dp[start_index][end_index - 1])
	return dp[0][input_str_len - 1]


print(find_lps_length_tabulation("abdbca"))
print(find_lps_length_tabulation("cddpd"))
print(find_lps_length_tabulation("pqr"))
