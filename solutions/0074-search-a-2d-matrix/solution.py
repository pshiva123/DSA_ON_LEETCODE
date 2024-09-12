class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        ceil=0
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if(matrix[mid][m-1]>target):
                #print(mid)
                ceil=mid
                high=mid-1
            elif(matrix[mid][m-1]==target):
                return True
            else:
                low=mid+1
        low=0
        print(ceil)
        high=len(matrix[0])-1

        while(low<=high):
            mid=(low+high)//2
            if(matrix[ceil][mid]==target):
                return True
            elif(matrix[ceil][mid]>target):
                high=mid-1
            else:
                low=mid+1
        return False


        
