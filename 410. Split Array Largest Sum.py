# the Problem is same as Book Allocation
# Painter Partition Problem Also same these problem
class Solution:
    def calculateStudent(self, A, pages):
        stu , pagesStudent = 1, 0
        for i in range(len(A)):
            if pagesStudent + A[i] <= pages:
                pagesStudent += A[i]
            else:
                stu += 1
                pagesStudent = A[i]
        return stu
    def findPages(self,A, M):
        #code here
        if M > len(A):
            return -1
        low , high = max(A), sum(A)
        while low <= high:
            mid = (low+high)//2
            if self.calculateStudent(A, mid) > M:
                low = mid + 1
            else:
                high = mid - 1
        return low
    def splitArray(self, nums: List[int], k: int) -> int:
        return self.findPages(nums, k)
        