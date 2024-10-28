class Solution:
    def findMaxConsecutiveOnes(self, arr: List[int]) -> int:
        maxi=0
        c=0
        for i in range(len(arr)):
            if arr[i]==1:
                c+=1
            else:
                maxi=max(c,maxi)
                c=0
        return max(maxi,c)
        
