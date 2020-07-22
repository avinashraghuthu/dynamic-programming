"""
Given a string, find the minimum number of characters that we
can remove to make it a palindrome.

Example 1:

Input: "abdbca"
Output: 1
Explanation: By removing "c", we get a palindrome "abdba".
"""


def find_min_deletion_pallindrome(input_str):
	return len(input_str) - find_lps_length(input_str)


def find_lps_length(input_str):
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


print(find_min_deletion_pallindrome("abdbca"))
print(find_min_deletion_pallindrome("cddpd"))
print(find_min_deletion_pallindrome("pqr"))
