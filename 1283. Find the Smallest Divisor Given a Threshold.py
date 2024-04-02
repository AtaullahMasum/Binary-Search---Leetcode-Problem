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