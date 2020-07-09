"""
Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing
the fee that you have to pay if you take the step. Implement a method to
calculate the minimum fee required to reach the top of the staircase
(beyond the top-most step). At every step, you have an option to take
either 1 step, 2 steps, or 3 steps. You should assume that you are
standing at the first step.

Number of stairs (n) : 6
Fee: {1,2,5,2,1,2}
Output: 3
Explanation: Starting from index '0', we can reach the top through: 0->3->top
The total fee we have to pay will be (1+2).
"""


def min_jumps_fee(fee_arr):
	fee_arr_len = len(fee_arr)
	dp = [0 for _ in range(fee_arr_len + 1)]
	dp[0] = 0  # no cost to take 0 steps
	dp[1] = fee_arr[0]  # include fee at 0 since we are taking that step with 1 step jump
	dp[2] = fee_arr[0]  # include fee at 0 since we are taking that step with 2 step jump
	for i in range(3, fee_arr_len + 1):
		# here dp is storing the cost until previous step since we haven't used that step
		# to move ahead.So to calculate we need to add the current step plus previous total.
		# Another thing is if i represent the current index for dp,then i-1 represent the
		# current index for fee_arr as its index based where as dp we are storing by number based.
		dp[i] = min(fee_arr[i - 1] + dp[i - 1],
					fee_arr[i - 2] + dp[i - 2],
					fee_arr[i - 3] + dp[i - 3])
	return dp[fee_arr_len]


print(min_jumps_fee([1, 2, 5, 2, 1, 2]))
print(min_jumps_fee([2, 3, 4, 5]))
