#Brute Force Approch
# Time Complexity is O((sum-max)*n)
class Solution: 
    # claculate number of students allocation  these book
    def calculateStudent(self, A, pages):
        stu , pagesStudent = 1, 0
        for i in range(len(A)):
            if pagesStudent + A[i] <= pages:
                pagesStudent += A[i]
            else:
                stu += 1
                pagesStudent = A[i]
        return stu
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if M > N:
            return -1
        low , high = max(A), sum(A)
        for pages in range(low , high+1):
            cntStu = self.calculateStudent(A, pages)
            if cntStu == M:
                return pages
#Optimal Solution Using Binary Search

