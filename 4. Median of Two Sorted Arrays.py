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
# Better Solution 
# Time Complexity O(n+m)
# Space Complexity O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        total = (n+m)
        index2 = total//2
        index1 = index2 - 1
        element1, element2 = -1,-1
        cnt = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                if cnt == index1:
                    element1 = nums1[i]
                if cnt == index2:
                    element2 = nums1[i]
                cnt += 1
                i += 1
            else:
                if cnt == index1:
                    element1 = nums2[j]
                if cnt == index2:
                    element2 = nums2[j]
                cnt += 1
                j += 1
        while i < n:
            if cnt == index1:
                element1 = nums1[i]
            if cnt == index2:
                element2 = nums1[i]
            cnt += 1
            i += 1
        while j < m:
            if cnt == index1:
                element1 = nums2[j]
            if cnt == index2:
                element2 = nums2[j]
            cnt += 1
            j += 1
        if (n+m)%2==1:
            return float(element2)
        else:
            return (element1+element2)/2.0