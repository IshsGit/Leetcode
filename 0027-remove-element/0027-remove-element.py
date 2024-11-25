class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize the pointer to place non-val elements
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Place it at position k and move the pointer
                nums[k] = nums[i]
                k += 1
        
        # k represents the number of elements in nums which are not equal to val
        return k
