class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right  = 0 , len(nums)-1
        ans = float('inf')
        while left <= right:
            mid = (left+right)//2
            #if left half is sorted then left half is eliminated but ans is save
            if nums[left]<= nums[mid]: 
                ans = min(ans, nums[left])
                left = mid + 1
            #else right half is sorted then right half is eliminated but ans is save
            else:
                ans = min(ans, nums[mid])
                right = mid - 1
        return ans
        