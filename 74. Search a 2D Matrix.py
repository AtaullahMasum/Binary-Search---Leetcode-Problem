#Brute Force Approch
#Time complexity O(n*m)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False
#Using Binary Search
#Time Complexity is O(nlogm)