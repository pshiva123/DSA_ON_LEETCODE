class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans=[]
        
        for row in matrix:
            ans.append(row.count(1))
        return ans
            
        
