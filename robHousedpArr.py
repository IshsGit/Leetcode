class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:

        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
