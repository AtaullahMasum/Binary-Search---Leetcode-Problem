# Iterative way
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1
        return -1
# Recursive Way
class Solution:
    def binarySearch(self, nums, left, right, target):
        if left > right:
            return -1
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(nums, left, mid-1, target)
        else:
            return self.binarySearch(nums, mid+1, right, target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)