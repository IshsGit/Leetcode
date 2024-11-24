class Solution:
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                permutations.append(nums[:])
            else:
                for i in range(start, end):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1, end)
                    nums[start], nums[i] = nums[i], nums[start]  # Backtrack

        permutations = []
        backtrack(0, len(nums))
        return permutations

# Test the function
solution = Solution()
print(solution.permute([1, 2, 3]))
