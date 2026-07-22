class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        result = nums1 + nums2
        result.sort()

        n = len(result)
        mid = n // 2

        if n % 2 == 1:     
            return result[mid]
        else:               # Even number of elements
            return (result[mid - 1] + result[mid]) / 2.0
