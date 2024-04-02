# Brute Force Approch
# Time Complexity O(m*n) where m is maximum element and n is number of element in the array
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maximum = max(nums)
        for d in range(1, maximum+1):
            sum = 0
            for i in range(len(nums)):
                sum += (nums[i]+d-1)//d
            if sum <= threshold:
                return d
        return -1
# Using Binary Search
# Time Complexity is O(nlongm) where n is number of element in the array and m is maximum element in these array
class Solution:
    def sumDivisor(self, nums, d):
        sum = 0
        for i in range(len(nums)):
            sum += (nums[i]+d-1)//d #always take ceil value
        return sum
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high =1,  max(nums)
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if self.sumDivisor(nums, mid) <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return low
        