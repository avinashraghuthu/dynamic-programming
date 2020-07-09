"""
Given a stair with ‘n’ steps, implement a method to count how many
possible ways are there to reach the top of the staircase, given that,
at every step you can either take 1 step, 2 steps, or 3 steps.

Number of stairs (n) : 3
Number of ways = 4
Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3}
"""


def stair_case(no_of_steps):
	dp = [0 for _ in range(no_of_steps + 1)]
	dp[0] = 1  # for 0 steps , there is only one way
	dp[1] = 1  # for 1 step, we can take only 1 step
	dp[2] = 2  # for 2 steps, we can (1,1) steps or (2) steps
	for i in range(3, no_of_steps + 1):
		dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
	return dp[no_of_steps]


print(stair_case(3))
print(stair_case(4))
print(stair_case(5))
