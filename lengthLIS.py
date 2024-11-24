class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
