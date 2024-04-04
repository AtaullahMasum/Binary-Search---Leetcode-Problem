#Brute Force Approch
#Time Complexity: O(k*n)
class Solution:
    def findSmallestMaxDist(self, stations, K):
        n = len(stations)
        howmany = [0]*(n-1)
        for gasStation in range(1, K+1):
            maxSection , maxIndex = -1, -1
            for i in range(len(howmany)):
                diff = stations[i+1] - stations[i]
                sectionLength = diff/(howmany[i]+1)
                if maxSection < sectionLength:
                    maxSection = sectionLength
                    maxIndex = i
            howmany[maxIndex] += 1
        maxAns = -1
        for i in range(len(howmany)):
            sectionLength = (stations[i+1] - stations[i])/(howmany[i]+1)
            maxAns = max(maxAns, sectionLength)
        return maxAns
#Using Maxheap
#Time Complexity is O(nlong + klogn)
#Space Complexity is O(n-1)
import heapq
from decimal import Decimal
class Solution:
    def findSmallestMaxDist(self, stations, K):
        n = len(stations)
        howmany = [0]*(n-1)
        heap = []
        for i in range(len(howmany)):
            diff = stations[i+1] - stations[i]
            heapq.heappush(heap, (-diff, i))
            
        for gasStation in range(1, K+1):
            diff, index = heapq.heappop(heap)
            howmany[index] += 1
            iniDiff = stations[index+1] - stations[index]
            sectionLength = iniDiff/(howmany[index]+1)*1.0
            heapq.heappush(heap, (-Decimal(sectionLength), index))
            
        maxAns, index = heapq.heappop(heap)
        maxAns = -float(maxAns)
        return maxAns
#Using Binary Search
import math
class Solution:
    def numberOfGasStationRequired(self, stations, dist):
        count = 0
        for i in range(len(stations)-1):  
            count += math.floor((stations[i+1] - stations[i])/dist)
        return count
            
    def findSmallestMaxDist(self, stations, K):
        low , high = 0, 0
        for i in range(len(stations)-1):
            high = max(high, stations[i+1]-stations[i])
        while high - low > 1e-6:
            mid = (low+high)/2.0
            if self.numberOfGasStationRequired(stations, mid)>K:
                low = mid
            else:
                high = mid
        return high