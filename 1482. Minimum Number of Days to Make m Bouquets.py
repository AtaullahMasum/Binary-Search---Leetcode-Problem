#Brute Force Approch
#Time Complexity O(n(max-min)) = O(n^2) where n is the length of the Array and 
#min and max are the Minimum and Maximum Blooday of the Array
class Solution:
    def possible(self, bloomDay, day, m, k):
        count, noOfB = 0, 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                count += 1
            else:
                noOfB += (count//k)
                count = 0
        noOfB += (count//k)
        if noOfB >= m:
            return True
        else:
            return False
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Impossible Case
        if len(bloomDay) < m*k:
            return -1
        minDay , maxDay = min(bloomDay), max(bloomDay)
        for day in range(minDay, maxDay+1):
            if self.possible(bloomDay, day, m, k):
                return day
        return -1
#Optimal Solution
#Time Complexity is O(nlog(max-min))
class Solution:
    def possible(self, bloomDay, day, m, k):
        count, noOfB = 0, 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                count += 1
            else:
                noOfB += (count//k)
                count = 0
        noOfB += (count//k)
        if noOfB >= m:
            return True
        else:
            return False
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Impossible Case
        if len(bloomDay) < m*k:
            return -1
        low , high = min(bloomDay), max(bloomDay) 
        ans = high
        while low <= high:
            mid = (low + high)//2
            if self.possible(bloomDay, mid, m, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1 
        return low
        
        