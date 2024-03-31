class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = float('inf')
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[left] == nums[mid] == nums[right]:
                ans = min(ans, nums[left])
                left = left + 1
                right = right -1
            elif nums[left]<= nums[mid]:
                ans = min(ans, nums[left])
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        return ans
