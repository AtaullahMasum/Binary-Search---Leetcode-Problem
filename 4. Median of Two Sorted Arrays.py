# Brute Force Approch 
# Time Complexity is O(n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        nums = []
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < n:
            nums.append(nums1[i])
            i += 1
        while j < m:
            nums.append(nums2[j])
            j += 1
        if (n+m)%2==1:
            return float(nums[(n+m)//2])
        else:
            return (nums[(n+m)//2-1]+nums[(n+m)//2])/2.0