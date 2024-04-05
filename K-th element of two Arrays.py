#Using Binary Search

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n > m:
            return self.kthElement(arr2, arr1, m, n, k)
        left = k
        low, high = max(0, k-m), min(k,n)
        while low <= high:
            mid1 = (low+high)//2
            mid2 = left - mid1
            l1, l2 = float('-inf'), float('-inf')
            r1, r2 = float('inf'), float('inf')
            if mid1 - 1 >= 0:
                l1 = arr1[mid1-1]
            if mid2 - 1 >= 0:
                l2 = arr2[mid2-1]
            if mid1 < n:
                r1 = arr1[mid1]
            if mid2 < m:
                r2 = arr2[mid2]
            if l1 <= r2 and l2 <= r1:
                return max(l1,l2)
            elif l1 > r2:
                high = mid1 -1
            else:
                low = mid1 + 1
            