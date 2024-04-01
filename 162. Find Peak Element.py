#Brute force Approch
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
       
        for i in range(len(nums)):
            if i == 0 and float('-inf') < nums[i] > nums[i+1]:
                return i
            if i == len(nums)-1 and nums[i-1]<nums[i] > float('-inf'):
                return i
            if nums[i-1]< nums[i] > nums[i+1]:
                return i
        