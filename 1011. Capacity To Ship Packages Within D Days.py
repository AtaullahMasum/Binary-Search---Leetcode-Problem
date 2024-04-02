#Brute Force Approch 
#Time Complexity O((sum-max)*n) where sum = all weights sum and max = maximum weights
# n is total number of elements
class Solution:
    def dayRequired(self, weights, capacity):
        day = 1
        loads = 0
        for i in range(len(weights)):
            if loads + weights[i] > capacity:
                day += 1
                loads = weights[i]
            else:
                loads += weights[i]
        return day
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCapacity, maxCapacity = max(weights) , sum(weights)
        for capacity in range(minCapacity, maxCapacity+1):
            dayReq = self.dayRequired(weights, capacity)
            if dayReq <= days:
                return capacity
        return -1
#Using Binary Search
# Time complexity O((sum-max)*logn)
class Solution:
    def dayRequired(self, weights, capacity):
        day = 1
        loads = 0
        for i in range(len(weights)):
            if loads + weights[i] > capacity:
                day += 1
                loads = weights[i]
            else:
                loads += weights[i]
        return day
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low , high = max(weights), sum(weights)
        while low <= high:
            mid = (low + high)//2
            if self.dayRequired(weights, mid) <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
        