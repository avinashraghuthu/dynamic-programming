"""
Given a string, find the length of its Longest Palindromic Substring (LPS).
In a palindromic string, elements read the same backward and forward.

Example 1:

Input: "abdbca"
Output: 3
Explanation: LPS is "bdb".
"""


def find_lps_length(input_str):
	input_str_len = len(input_str)
	dp = [[False for _ in range(input_str_len)] for _ in range(input_str_len)]
	
	for i in range(input_str_len):
		dp[i][i] = True
	max_length = 1
	for start_index in range(input_str_len - 1, -1, -1):
		for end_index in range(start_index + 1, input_str_len):
			if input_str[start_index] == input_str[end_index]:
				if end_index - start_index == 1 or dp[start_index + 1][end_index - 1]:
					dp[start_index][end_index] = True
					max_length = max(max_length, end_index - start_index + 1)
	return max_length


print(find_lps_length("abdadba"))
print(find_lps_length("cddpd"))
print(find_lps_length("pqr"))
