# Brute Force Approch
# Time Complexity is : O((max_stalls-min_stalls+1)*n)
class Solution:
    def canBePlace(self, stalls, dist, k, n):
        cntCows , last = 1, stalls[0]
        for i in range(1, n):
            if stalls[i] - last >= dist:
                cntCows += 1
                last = stalls[i]
        if cntCows >= k:
            return True
        else:
            return False
    
    def solve(self,n,k,stalls):
        min_stalls , max_stalls = min(stalls) , max(stalls)
        for i in range(1, (max_stalls -min_stalls)):
            if self.canBePlace(stalls, i, k, n):
                continue
            else:
                return i-1
# Optimal Solution Binary Search 
# Timw complexity O(nlog(max-min))
class Solution:
    def canBePlace(self, stalls, dist, k, n):
        cntCows , last = 1, stalls[0]
        for i in range(1, n):
            if stalls[i] - last >= dist:
                cntCows += 1
                last = stalls[i]
        if cntCows >= k:
            return True
        else:
            return False
    
    def solve(self,n,k,stalls):
        stalls.sort()
        low , high = 1, max(stalls) - min(stalls)
        while low <= high:
            mid = (low+high)//2
            if self.canBePlace(stalls, mid, k, n):
                low = mid + 1
            else:
                high = mid - 1
        return high
            

       