class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        row=0
        left=0
        right=n-1
        li=[]
        i=0
        while(len(li)<=(m*n)):
            while(left<=right):
                li.append(matrix[row][left])
                left+=1
            left-=1
            row+=1
            if len(li)==(m*n):
                break
            while(row<=m-i-1):
                li.append(matrix[row][right])
                row+=1
            row-=1
            right-=1
            if len(li)==(m*n):
                break
            while(right>=i):
                #print(row,right)
                li.append(matrix[row][right])
                right-=1
            right+=1
            row-=1
            if len(li)==(m*n):
                break
            while(row>i):
                li.append(matrix[row][right])
                row-=1
            if len(li)==(m*n):
                break
            row+=1
            i+=1
            left=i
            right=n-i-1
        return li


        
        
        
