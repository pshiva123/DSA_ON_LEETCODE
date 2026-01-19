class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n=len(mat)
        m=len(mat[0])
        for i in range(1,m):
            mat[0][i]=mat[0][i]+mat[0][i-1]
        for i in range(1,n):
            mat[i][0]=mat[i][0]+mat[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                mat[i][j]+=mat[i-1][j]+mat[i][j-1]-mat[i-1][j-1]
        for row in mat:
            print(*row)
        ans=0
        l=1
        h=min(m,n)
        while l<=h:
            mid=(l+h)//2
            if f(mat,mid,n,m,threshold):
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans
def f(arr, mid, n, m, k):
    for i in range(n - mid + 1):
        for j in range(m - mid + 1):
            r2 = i + mid - 1
            c2 = j + mid - 1

            total = arr[r2][c2]

            if i > 0:
                total -= arr[i - 1][c2]
            if j > 0:
                total -= arr[r2][j - 1]
            if i > 0 and j > 0:
                total += arr[i - 1][j - 1]

            if total <= k:
                return True
    return False

        

        
