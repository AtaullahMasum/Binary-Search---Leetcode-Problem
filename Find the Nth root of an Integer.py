class Solution:
    def myPow(self, x, n):
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result
    
    def NthRoot(self, n, m):
        for i in range(m + 1):  # Include m as well in the range.
            power = self.myPow(i, n)
            if power == m:
                return i
            elif power > m:
                break
        return -1
# Time Complexity is O(mlongn)
#Using Binary Search 
class Solution:
    def myPow(self, x, n):
        result = 1
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        return result
    
    def NthRoot(self, n, m):
        low, high  = 1, m
        while low <= high:
            mid =(low+high)//2
            if self.myPow(mid, n) == m:
                return mid
            elif self.myPow(mid, n) > m:
                high = mid - 1
            else:
                low = mid + 1
        return -1
# Time Complexity is O(logmlong)