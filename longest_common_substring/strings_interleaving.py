def find_strings_interleaving(input_str_m, input_str_n, output_str_p):
	input_str_m_len = len(input_str_m)
	input_str_n_len = len(input_str_n)
	output_str_p_len = len(output_str_p)
	if input_str_m_len + input_str_n_len != output_str_p_len:
		return False
	dp = [[False for _ in range(input_str_n_len+1)] for _ in range(input_str_m_len+1)]
	for m_index in range(input_str_m_len+1):
		for n_index in range(input_str_n_len+1):
			if m_index == 0 and n_index == 0:
				dp[m_index][n_index] = True
			elif m_index ==0 and input_str_n[n_index-1] == output_str_p[m_index+n_index-1]:
				dp[m_index][n_index] = dp[m_index][n_index-1]
			elif n_index ==0 and input_str_m[m_index-1] == output_str_p[m_index+n_index-1]:
				dp[m_index][n_index] = dp[m_index-1][n_index]
			else:
				if m_index > 0 and input_str_m[m_index-1] == output_str_p[m_index+n_index-1]:
					dp[m_index][n_index] = dp[m_index-1][n_index]
				if n_index > 0 and input_str_n[n_index-1] == output_str_p[m_index+n_index-1]:
					dp[m_index][n_index] |= dp[m_index][n_index-1]
	return dp[input_str_m_len][input_str_n_len]


print(find_strings_interleaving("abd", "cef", "abcdef"))
print(find_strings_interleaving("abd", "cef", "adcbef"))
print(find_strings_interleaving("abc", "def", "abdccf"))
print(find_strings_interleaving("abcdef", "mnop", "mnaobcdepf"))