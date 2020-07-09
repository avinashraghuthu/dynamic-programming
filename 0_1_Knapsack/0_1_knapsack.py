"""
Given two integer arrays to represent weights and profits of 'N' items,
we need to find a subset of these items which will give us maximum profit
such that their cumulative weight is not more than a given number 'C'.
Each item can only be selected once, which means either we put an item in
the knapsack or we skip it.
"""


# Method 1 - recursion
def solve_knapsack_recursion(profits, weights, capacity):
	return knapsack_recursion_utils(profits, weights, capacity, 0)


def knapsack_recursion_utils(profits, weights, capacity, current_index):
	if capacity <= 0 or current_index >= len(profits):
		return 0
	
	profit1 = 0
	if weights[current_index] <= capacity:
		profit1 = profits[current_index] + knapsack_recursion_utils(profits, weights,
																	capacity - weights[current_index],
																	current_index + 1)
	
	profit2 = knapsack_recursion_utils(profits, weights, capacity, current_index + 1)
	return max(profit1, profit2)


# Method 2 - DP Top Down Approach
def solve_knapsack_dp_memoization(profits, weights, capacity):
	dp = [[-1 for j in range(capacity + 1)] for i in range(len(profits))]
	return knapsack_dp_memoization_utils(dp, profits, weights, capacity, 0)


def knapsack_dp_memoization_utils(dp, profits, weights, capacity, current_index):
	if capacity <= 0 or current_index >= len(profits):
		return 0
	
	if dp[current_index][capacity] != -1:
		return dp[current_index][capacity]
	
	profit1 = 0
	if weights[current_index] <= capacity:
		profit1 = profits[current_index] + knapsack_dp_memoization_utils(dp, profits, weights,
																		 capacity - weights[current_index],
																		 current_index + 1)
	profit2 = knapsack_dp_memoization_utils(dp, profits, weights, capacity, current_index + 1)
	dp[current_index][capacity] = max(profit1, profit2)
	return dp[current_index][capacity]


# Method 3 - DP Bottom Up Approach
def solve_knapsack_dp_tabulation(profits, weights, capacity):
	no_of_items = len(profits)
	
	if no_of_items <= 0 or capacity <= 0 or no_of_items != len(weights):
		return 0
	
	dp = [[0 for j in range(capacity + 1)] for i in range(no_of_items)]
	
	for i in range(no_of_items):
		dp[i][0] = 0
	
	for c in range(capacity + 1):
		if weights[0] <= c:
			dp[0][c] = profits[0]
	
	for i in range(1, no_of_items):
		for c in range(1, capacity + 1):
			profit1 = 0
			if weights[i] <= c:
				profit1 = profits[i] + dp[i - 1][c - weights[i]]
			profit2 = dp[i - 1][c]
			dp[i][c] = max(profit1, profit2)
	print_selected_elements(dp, weights, profits, capacity)
	return dp[no_of_items - 1][capacity]


def print_selected_elements(dp, weights, profits, capacity):
	print("weights for tabulation: ", end=" ")
	no_of_items = len(weights)
	total_profit = dp[no_of_items - 1][capacity]
	for i in range(no_of_items - 1, 0, -1):
		if total_profit != dp[i - 1][capacity]:
			print(weights[i], end=" ")
			total_profit -= profits[i]
			capacity -= weights[i]
	if total_profit != 0:
		print(weights[0], end=" ")


print("Recursion: ", solve_knapsack_recursion([1, 6, 10, 16], [1, 2, 3, 5], 7))
print("Memoization: ", solve_knapsack_dp_memoization([1, 6, 10, 16], [1, 2, 3, 5], 7))
print("Tabulation: ", solve_knapsack_dp_tabulation([1, 6, 10, 16], [1, 2, 3, 5], 7))
