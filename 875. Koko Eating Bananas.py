class Solution:
    def calculateHour(self, piles, hour):
        total_hour = 0
        for i in range(len(piles)):
            total_hour += (piles[i] + hour - 1) // hour #because always taking ceil value so hour - 1 added
        return total_hour
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1, max(piles)
        while low <= high:
            mid = (low + high)//2
            if self.calculateHour(piles, mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
#time complexity is O(nlogm) where n is number of piles and m is 1 to maximum number of piles