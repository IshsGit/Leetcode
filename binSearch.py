from bisect import bisect_right

def job_scheduling(startTime, endTime, profit):
    jobs = sorted(zip(endTime, startTime, profit))
    dp = [(0, 0)]

    for e, s, p in jobs:
        i = bisect_right(dp, (s, float('inf'))) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append((e, dp[i][1] + p))

    return dp[-1][1]
