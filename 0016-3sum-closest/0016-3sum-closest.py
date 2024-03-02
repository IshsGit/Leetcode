class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        closest_sum = float('inf')  # Initialize closest sum to positive infinity
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # Update closest sum if necessary
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                # Move pointers based on the comparison with target
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # If sum is equal to target, return immediately
        
        return closest_sum