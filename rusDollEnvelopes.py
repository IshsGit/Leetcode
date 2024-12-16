def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    def lis(arr):
        dp = []
        for num in arr:
            lo, hi = 0, len(dp)
            while lo < hi:
                mid = (lo + hi) // 2
                if dp[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(dp):
                dp.append(num)
            else:
                dp[lo] = num
        return len(dp)

    return lis([e[1] for e in envelopes])
