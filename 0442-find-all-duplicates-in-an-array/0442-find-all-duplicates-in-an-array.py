class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return []
        
        freq={}
        for el in nums:
            if el not in freq:
                freq[el]=1
            else:
                freq[el]+=1
                
        twice=[]
        for key in freq:
            if freq[key]==2:
                twice.append(key)
        return twice