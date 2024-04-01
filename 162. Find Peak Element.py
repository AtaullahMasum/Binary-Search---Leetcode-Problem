#Brute force Approch
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       
        for i in range(len(nums)):
           if (i == 0 or nums[i-1]<nums[i] ) and (i ==len(nums)-1 or nums[i]>nums[i+1]):
            return i

#Using Binary Search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] >nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums)-1
        low , high = 1, len(nums) - 2
        while low <= high:
            mid = (low+high)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

      
