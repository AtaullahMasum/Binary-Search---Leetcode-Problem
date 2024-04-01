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