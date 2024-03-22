class Solution:

    def search(self,nums,target):
        if len(nums) == 1:
            if nums[0] != target:
                return False
            else:
                return True

        midpoint = int((len(nums)/2)//1)
        left = nums[:midpoint]
        right = nums[midpoint:]

        leftSearch = self.search(left, target)
        if leftSearch == False:
            rightSearch = self.search(right, target)
            if rightSearch != False:
                return True
            else:
                return rightSearch
        else:
            return leftSearch



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if self.search(arr, target) == True:
                return True

        return False
