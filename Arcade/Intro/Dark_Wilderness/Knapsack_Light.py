def solution(value1, weight1, value2, weight2, maxW):
    # Initialize a 2D table for dynamic programming
    dp = [[0] * (maxW + 1) for _ in range(3)]

    for i in range(1, 3):
        for j in range(1, maxW + 1):
            # Skip the item if it exceeds the current weight capacity
            if (i == 1 and j < weight1) or (i == 2 and j < weight2):
                dp[i][j] = dp[i-1][j]
            else:
                # Take the maximum value of either skipping the item or taking the item
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight1] + value1) if i == 1 else max(dp[i-1][j], dp[i-1][j - weight2] + value2)

    return dp[2][maxW]

