# Write a function to solve the 0/1 Knapsack problem using dynamic programming.


def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][capacity]


weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6
print(knapsack(weights, values, capacity))
