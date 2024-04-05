# Using Binary Search
# Time Complexity is O()
class Solution:
    def findMaxIndex(self,mat, n, col):
        index = -1
        maxValue = -1
        for i in range(n):
            if mat[i][col] > maxValue:
                maxValue = mat[i][col]
                index = i
        return index
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n , m = len(mat), len(mat[0])
        low , high = 0, m-1
        while low <= high:
            mid =(low + high )//2
            maxRowIndex = self.findMaxIndex(mat, n, mid )
            left, right = -1, -1
            if mid - 1 >= 0:
                left = mat[maxRowIndex][mid-1]
            if mid + 1 < m:
                right = mat[maxRowIndex][mid+1]
            if  left <mat[maxRowIndex][mid] > right:
                return [maxRowIndex, mid]
            elif mat[maxRowIndex][mid] > left:
                low = mid + 1
            else:
                high = mid -1
        return [-1, -1]
        