class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0):
            if start == len(nums):
                res.append(nums[:])
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        nums.sort()
        res = []
        backtrack()
        return res
