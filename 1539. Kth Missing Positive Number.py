#Using Brute Force
#Time Complexity O(n)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k
#Optimal Solution Added
# Time Complexity is O(logn)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low , high = 0, len(arr)-1
        while low <= high:
            mid = (low+high)//2
            missing = arr[mid] -(mid+1)
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return high + 1 + k 
        