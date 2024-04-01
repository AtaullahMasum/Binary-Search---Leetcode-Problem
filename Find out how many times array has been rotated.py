class Solution:
    def findMin(self, nums: List[int]) -> int:
        left , right  = 0 , len(nums)-1
        ans = float('inf')
        index = -1
        while left <= right:
            mid = (left+right)//2
            #if array is already sorted then nums[left] is minimum element in the array 
            # and these index is the answer
            if nums[left] <= nums[right]:
                if ans > nums[left]:
                    ans = min(ans, nums[left])
                    index = left 
                break 
            #if left half is sorted then left half is eliminated but ans is save
            if nums[left]<= nums[mid]:
                if ans > nums[left]:
                    ans = min(ans, nums[left])
                    index = left    
                left = mid + 1
            #else right half is sorted then right half is eliminated but ans is save
            else:
                if ans > nums[left]:
                    ans = min(ans, nums[left])
                    index = right
                right = mid - 1
        return index
        