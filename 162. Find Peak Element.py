#Brute force Approch
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        for i in range(len(nums)-1):
            if nums[i-1]< nums[i] > nums[i+1]:
                return i