"""
Write a function to calculate the nth Fibonacci number.

Fibonacci numbers are a series of numbers in which each number is the sum
of the two preceding numbers. First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …
"""

# Method 1: recursion
def fibnocci_recursion(number):
	if number < 2:
		return number
	return fibnocci_recursion(number - 1) + fibnocci_recursion(number - 2)


# Method 2: Top Down Approach - Memoization
def fibnocci_memoization(number):
	dp = [-1 for _ in range(number + 1)]
	return fibnocci_memoization_utils(dp, number)


def fibnocci_memoization_utils(dp, number):
	if number < 2:
		return number
	
	if dp[number] != -1:
		return dp[number]
	
	dp[number] = fibnocci_memoization_utils(dp, number - 1) + \
				 fibnocci_memoization_utils(dp, number - 2)
	return dp[number]


# Method 3 - Bottom Up Approach - Tabulation
def fibnocci_tabulation(number):
	dp = [0 for _ in range(number+1)]
	dp[0] = 0
	dp[1] = 1
	for i in range(2, number+1):
		dp[i] = dp[i-1] + dp[i-2]
	return dp[number]

print("5th Fibonacci using fibnocci_recursion is ---> " + str(fibnocci_recursion(5)))
print("5th Fibonacci using fibnocci_memoization is ---> " + str(fibnocci_memoization(5)))
print("6th Fibonacci using fibnocci_memoization is ---> " + str(fibnocci_memoization(6)))
print("7th Fibonacci using fibnocci_memoization is ---> " + str(fibnocci_memoization(7)))
print("7th Fibonacci using fibnocci_tabulation is ---> " + str(fibnocci_tabulation(7)))
