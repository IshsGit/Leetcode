def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    wordSet = set(wordDict)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[-1]