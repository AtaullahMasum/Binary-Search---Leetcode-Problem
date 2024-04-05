#Brute Force Approch
#Time complexity O(n*m)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
#Using Binary Search Row wise
#Time Complexity is O(n) + log(m)
class Solution:
    def binarySearch(self, arr, m, target):
        low , high = 0 , m-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high = mid -1
            else:
                low = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n , m = len(matrix), len(matrix[0])
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                if self.binarySearch(matrix[i], m, target):
                    return True
        return False
#Using Binary Search Entire Matrix
# Time Complexity is O(log(m*n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        total = rows*cols
        low, high = 0, total-1
        while low <= high:
            mid = (low+high)//2
            row , col = mid//cols, mid%cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False