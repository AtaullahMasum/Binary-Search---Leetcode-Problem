#User function Template for python3
# Using Binary Search
# Time Complesity is O(log(max-min)*nlogm) where n is number of row and m is the number of column 
# and max and min is the maximum and minimum number of the given matrix

class Solution:
    # these upper bound return number of element less than x in that row
    def upperBound(self, arr, x):
        low , high = 0, len(arr)-1
        ans = len(arr)
        while low <= high:
            mid = (low+high)//2
            if arr[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    # these blackBox calcaulate total number of element less than  that number 
    # and return total number less than x
    def blackBox(self, matrix, R,  x):
        cnt = 0
        for i in range(R):
            cnt += self.upperBound(matrix[i], x)
        return cnt
        
    def median(self, matrix, R, C):
        #code here
        # min_val and max_val calculate mimimum and maximum value in that matrix
        min_val = min(min(row) for row in matrix)
        max_val = max(max(row) for row in matrix)
        # median always middle position of total number of that matrix
        required = (R*C)//2
        low , high = min_val, max_val
        while low <= high:
            mid = (low+high)//2
            smallerRequired = self.blackBox(matrix,R, mid)
            # smaller required less than or equal required then move low to mid + 1
            # else move high to mid -1
            # return low 
            if smallerRequired <= required:
                low = mid + 1
            else:
                high = mid - 1
        return low