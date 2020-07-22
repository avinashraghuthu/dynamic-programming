"""
Given a string, we want to cut it into pieces such that each piece is a palindrome.
Write a function to return the minimum number of cuts needed.

Example 1:

Input: "abdbca"
Output: 3
Explanation: Palindrome pieces are "a", "bdb", "c", "a".
"""


def calculate_min_partitions(input_str):
	input_str_len = len(input_str)
	is_palindrome = [[False for _ in range(input_str_len)] for _ in range(input_str_len)]
	
	for i in range(input_str_len):
		is_palindrome[i][i] = True
	
	for start_index in range(input_str_len - 1, -1, -1):
		for end_index in range(start_index + 1, input_str_len):
			if input_str[start_index] == input_str[end_index]:
				if end_index - start_index == 1 or is_palindrome[start_index + 1][end_index - 1]:
					is_palindrome[start_index][end_index] = True
	
	cuts = [0 for _ in range(input_str_len)]
	for start_index in range(input_str_len - 1, -1, -1):
		min_cuts = input_str_len
		for end_index in range(input_str_len - 1, start_index - 1, -1):
			if is_palindrome[start_index][end_index]:
				min_cuts = 0 if end_index == input_str_len - 1 else \
					min(min_cuts, 1 + cuts[end_index + 1])  # checking for previous value in end_index+1
		cuts[start_index] = min_cuts
	return cuts[0]


print(calculate_min_partitions("abdbca"))
print(calculate_min_partitions("cdpdd"))
print(calculate_min_partitions("pqr"))
print(calculate_min_partitions("pp"))
print(calculate_min_partitions("madam"))
