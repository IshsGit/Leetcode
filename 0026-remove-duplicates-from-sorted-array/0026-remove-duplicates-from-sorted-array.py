class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize pointer for placing unique elements
        unique_index = 0
        
        # Iterate through the array
        for i in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[i] != nums[unique_index]:
                # Increment the pointer and place the current element
                unique_index += 1
                nums[unique_index] = nums[i]
        
        # The number of unique elements is one more than the unique_index
        return unique_index + 1