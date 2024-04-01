#Brute force Approch
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if i == 0:
                if nums[i] != nums[i+1]:
                    return nums[i]
            elif i == len(nums)-1:
                if nums[i] != nums[i-1]:
                    return nums[i]
            else:
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]
#Optimal Approch using Binary Search
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[len(nums)-1] != nums[len(nums)-2]:
            return nums[len(nums)-1]
        left = 1
        right = len(nums)-2
        while left<= right:
            mid =(left+right)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            #if element is the right half then eilminate left half
            if (mid%2 == 1 and nums[mid] == nums[mid-1]) or(mid%2 == 0 and nums[mid]==nums[mid+1]):
                left = mid + 1
            else: #if element is the left half then eilminate right half
                right = mid - 1

