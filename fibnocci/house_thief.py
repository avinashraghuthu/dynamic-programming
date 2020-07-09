"""
Given a number array representing the wealth of ‘n’ houses, determine
the maximum amount of money the thief can steal without alerting the security system.

Input: {2, 5, 1, 3, 6, 2, 4}
Output: 15
Explanation: The thief should steal from houses 5 + 6 + 4
"""


def house_thief(wealth_arr):
	no_of_houses = len(wealth_arr)
	dp = [0 for _ in range(no_of_houses + 1)]
	dp[0] = 0  # If no of houses are zero, then wealth will be 0
	dp[1] = wealth_arr[0]  # If no of houses are 1, that house will be wealth
	for i in range(2, no_of_houses + 1):
		# here wealth_arr[i-1] represents the current wealth as dp is doing by number based,
		# where as wealth_arr is index based.So if i represents the current index for dp then,
		# i-1 represent the current index for wealth_arr
		dp[i] = max(wealth_arr[i - 1] + dp[i - 2], dp[i - 1])
	return dp[no_of_houses]


print(house_thief([2, 5, 1, 3, 6, 2, 4]))
print(house_thief([2, 10, 14, 8, 1]))
