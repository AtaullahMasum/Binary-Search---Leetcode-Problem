class Solution:
    def lowerBound(self, nums:List[int], target: int)->int:
        lb = len(nums)
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    def upperBound(self, nums:List[int], target: int)->int:
        ub = len(nums)
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1,-1]
        ub = self.upperBound(nums, target)-1
        return [lb, ub]
        