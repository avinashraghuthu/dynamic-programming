"""
Given two integer arrays to represent weights and profits of ‘N’ items,
we need to find a subset of these items which will give us maximum profit
such that their cumulative weight is not more than a given number ‘C’.
We can assume an infinite supply of item quantities; therefore,
each item can be selected multiple times.

"""


# Method 1 - recursion
def solve_unbounded_knapsack_recursion(profits, weights, capacity):
	return solve_unbounded_knapsack_recursion_utils(profits, weights, capacity, 0)


def solve_unbounded_knapsack_recursion_utils(profits, weights, capacity, current_index):
	if capacity <= 0 or current_index >= len(profits):
		return 0
	
	profit1 = 0
	if weights[current_index] <= capacity:
		profit1 = profits[current_index] + solve_unbounded_knapsack_recursion_utils \
			(profits, weights, capacity - weights[current_index], current_index)
	profit2 = solve_unbounded_knapsack_recursion_utils(profits, weights,
													   capacity, current_index + 1)
	return max(profit1, profit2)


# Method 2 - DP Top Down Approach
def solve_unbounded_knapsack_memoization(profits, weights, capacity):
	dp = [[-1 for j in range(capacity + 1)] for i in range(len(profits))]
	return solve_unbounded_knapsack_memoization_utils(dp, profits, weights, capacity, 0)


def solve_unbounded_knapsack_memoization_utils(dp, profits, weights, capacity, current_index):
	if capacity <= 0 or current_index >= len(profits):
		return 0
	
	if dp[current_index][capacity] == -1:
		profit1 = 0
		if weights[current_index] <= capacity:
			profit1 = profits[current_index] + solve_unbounded_knapsack_memoization_utils(
				dp, profits, weights, capacity - weights[current_index], current_index)
		profit2 = solve_unbounded_knapsack_memoization_utils(
			dp, profits, weights, capacity, current_index + 1)
		dp[current_index][capacity] = max(profit1, profit2)
	return dp[current_index][capacity]


# Method 3 - DP Bottom Up Approach
def solve_unbounded_knapsack_tabulation(profits, weights, capacity):
	no_of_items = len(profits)
	if no_of_items == 0 or no_of_items != len(weights) or capacity <= 0:
		return 0
	
	dp = [[-1 for j in range(capacity + 1)] for i in range(no_of_items)]
	
	for i in range(no_of_items):
		dp[i][0] = 0
	
	for i in range(no_of_items):
		for c in range(1, capacity + 1):
			profit1, profit2 = 0, 0
			if weights[i] <= c:
				profit1 = profits[i] + dp[i][c - weights[i]]
			if i > 0:
				profit2 = dp[i - 1][c]
			dp[i][c] = max(profit1, profit2)
	return dp[no_of_items - 1][capacity]


print("Recursion:", solve_unbounded_knapsack_recursion([15, 50, 60, 90], [1, 3, 4, 5], 8))
print("Recursion:", solve_unbounded_knapsack_recursion([15, 50, 60, 90], [1, 3, 4, 5], 6))
print("Memoization:", solve_unbounded_knapsack_memoization([15, 50, 60, 90], [1, 3, 4, 5], 8))
print("Memoization:", solve_unbounded_knapsack_memoization([15, 50, 60, 90], [1, 3, 4, 5], 6))
print("Tabulation:", solve_unbounded_knapsack_tabulation([15, 50, 60, 90], [1, 3, 4, 5], 8))
print("Tabulation:", solve_unbounded_knapsack_tabulation([15, 50, 60, 90], [1, 3, 4, 5], 6))
