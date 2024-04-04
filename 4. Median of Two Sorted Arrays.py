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
#Using Binary Search
#Time Complexity is O(log(min(n1,n2)))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        low , high = 0, n1
        left = ( n1 + n2 + 1)//2
        n = n1 + n2
        while low <= high:
            mid1 = (low + high)//2
            mid2 = left - mid1
            l1 , r1 = float('-inf'), float('inf')
            l2 , r2 = float('-inf'), float('inf')
            if mid1 - 1 >= 0:
                l1 = nums1[mid1-1]
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2-1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if l1 <= r2 and l2 <= r1:
                if n%2==1:
                    return float(max(l1,l2))
                else:
                    return (max(l1,l2) + min(r1,r2))/2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0
