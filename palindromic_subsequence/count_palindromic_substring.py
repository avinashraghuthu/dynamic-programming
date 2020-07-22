"""
Given a string, find the total number of palindromic substrings in it.
Please note we need to find the total number of substrings and not subsequences.

Example 1:

Input: "abdbca"
Output: 7
Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".
"""


def count_ps(input_str):
	input_str_len = len(input_str)
	dp = [[False for _ in range(input_str_len)] for _ in range(input_str_len)]
	count = 0
	for i in range(input_str_len):
		dp[i][i] = True
		count += 1
	
	for start_index in range(input_str_len - 1, -1, -1):
		for end_index in range(start_index + 1, input_str_len):
			if input_str[start_index] == input_str[end_index]:
				if end_index - start_index == 1 or dp[start_index + 1][end_index - 1]:
					dp[start_index][end_index] = True
					count += 1
	return count


print(count_ps("abdbca"))
print(count_ps("cddpd"))
print(count_ps("pqr"))
print(count_ps("qqq"))
