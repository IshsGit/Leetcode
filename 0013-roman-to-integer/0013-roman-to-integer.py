class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        for idx, c in enumerate(s[:len(s)-1:]):
            if nums[c] >= nums[s[idx+1]]:
                result += nums[c]
            elif nums[c] < nums[s[idx+1]]:
                result -= nums[c]
        return result+nums[s[-1]]