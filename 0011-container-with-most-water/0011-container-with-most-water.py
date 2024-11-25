class Solution:
    def maxArea(self, height: List[int]) -> int:
       #if proceding element of start pointer is greater, then increment start pointer, and end pointer and          #stays the same
       #if preceding elemt of end pointer is greater, then decrement end pointer
     
        n=len(height)
        start=0
        end=n-1
        maxHeight=0
        while start<end:
            curr_area=area1=area2=area3=(end-start)*min(height[end],height[start])
            maxHeight=max(curr_area,maxHeight)
            if height[start]<height[end]:
                start+=1    
            else:
                end-=1       
        return maxHeight
        