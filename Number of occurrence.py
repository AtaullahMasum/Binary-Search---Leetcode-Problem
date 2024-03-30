#User function Template for python3
class Solution:
        def lowerBound(self, arr, n, x):
            low , high = 0,  n-1
            lb = n
            while low <= high:
                mid =(low+high)//2
                if arr[mid] >= x:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return lb
        def upperBound(self, arr, n, x):
            low, high = 0, n-1
            ub = n
            while low <= high:
                mid = (low + high)//2
                if arr[mid] > x:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ub 
        def count(self,arr, n, x):
            # code here
            lb = self.lowerBound(arr, n, x)
            if lb == n or arr[lb] != x:
                return 0
            ub = self.upperBound(arr, n, x)-1 #important 
            return ub - lb + 1