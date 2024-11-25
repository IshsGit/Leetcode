class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a dictionary to store computed results
        memo = {}

        # Recursive function with memoization
        def climb(n):
            if n in memo:
                return memo[n]
            if n == 1:
                result = 1
            elif n == 2:
                result = 2
            else:
                result = climb(n-1) + climb(n-2)
            
            # Store the result in the memo dictionary
            memo[n] = result
            return result

        return climb(n)

# Example usage:
# solution = Solution()
# result = solution.climbStairs(5)
# print(result)
