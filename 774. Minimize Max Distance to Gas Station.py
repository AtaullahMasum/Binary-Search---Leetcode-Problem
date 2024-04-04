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
            sectionLength = iniDiff/(howmany[index]+1)
            heapq.heappush(heap, (-Decimal(sectionLength), index))
            
        maxAns, index = heapq.heappop(heap)
        maxAns = -float(maxAns)
        return maxAns