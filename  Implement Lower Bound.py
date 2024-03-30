def lowerBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    floor = n
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= x:
            floor = mid
            high = mid -1 
        else:
            low = mid + 1
    return floor
#GFG Solution
class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        low, high = 0, N - 1
        floor_index = -1
        while low <= high:
            mid = (low + high) // 2
            if A[mid] <= X:
                floor_index = mid
                low = mid + 1
            else:
                high = mid - 1
        return floor_index
    