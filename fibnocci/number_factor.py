"""
Given a number ‘n’, implement a method to count how many possible
ways there are to express ‘n’ as the sum of 1, 3, or 4.

n : 4
Number of ways = 4
Explanation: Following are the four ways we can exoress 'n' : {1,1,1,1}, {1,3}, {3,1}, {4}
"""


def count_ways(number):
	dp = [0 for _ in range(number + 1)]
	dp[0] = 1
	dp[1] = 1
	dp[2] = 1
	dp[3] = 2
	for i in range(4, number + 1):
		dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]
	return dp[number]


print(count_ways(4))
print(count_ways(5))
print(count_ways(6))
