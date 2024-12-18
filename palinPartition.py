def minCut(s):
    n = len(s)
    dp = [float('inf')] * n
    pal = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if s[j:i + 1] == s[j:i + 1][::-1]:
                pal[j][i] = True
                dp[i] = 0 if j == 0 else min(dp[i], dp[j - 1] + 1)
    return dp[-1]