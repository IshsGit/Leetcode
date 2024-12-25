def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[-1] * cols for _ in range(rows)]

    def dfs(r, c, prev_val):
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev_val:
            return 0
        if dp[r][c] != -1:
            return dp[r][c]
        result = 1 + max(
            dfs(r + 1, c, matrix[r][c]),
            dfs(r - 1, c, matrix[r][c]),
            dfs(r, c + 1, matrix[r][c]),
            dfs(r, c - 1, matrix[r][c])
        )
        dp[r][c] = result
        return result

    return max(dfs(r, c, -float('inf')) for r in range(rows) for c in range(cols))
