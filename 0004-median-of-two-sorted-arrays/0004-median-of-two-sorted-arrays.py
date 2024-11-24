class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
  
        combined = sorted(nums1 + nums2)

        n = len(combined)
        if n % 2 == 1:  # odd length
            median = combined[n // 2]
        else:  # even length
            median = (combined[(n // 2) - 1] + combined[n // 2]) / 2.0

        return median

