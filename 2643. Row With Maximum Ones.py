# Brute Force Approch
# Time Complexity is O(nxm)
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index = -1
        maxCount = -1
        for i in range(len(mat)):
            countRows = 0
            for j in range(len(mat[0])):
                countRows += mat[i][j]
            if countRows > maxCount:
                maxCount = countRows
                index = i             
        return [index, maxCount]
# Using Binary Search
# Time Complexity is O(nlogm)
class Solution:
    def lowerBound(self, arr, n, k):
        low , high = 0, n-1
        ans = n
        while low<= high:
            mid = (low+high)//2
            if arr[mid] >= k:
                ans = mid
                high = mid - 1          
            else:
                low = mid + 1
        return ans
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index = 0
        cnt_Max = 0
        for i in range(len(mat)):
            cnt_ones = len(mat[0]) - self.lowerBound(sorted(mat[i]), len(mat[0]), 1)
            if cnt_ones > cnt_Max:
                cnt_Max = cnt_ones
                index = i
                
        return [index, cnt_Max]
        
        