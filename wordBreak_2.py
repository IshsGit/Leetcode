def wordBreak(s, wordDict):
    def helper(start, memo):
        if start == len(s):
            return [""]
        if start in memo:
            return memo[start]
        res = []
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict:
                for suffix in helper(end, memo):
                    res.append(s[slice(start, end)] + ("" if not suffix else " " + suffix))
        memo[start] = res
        return res

    return helper(0, {})
