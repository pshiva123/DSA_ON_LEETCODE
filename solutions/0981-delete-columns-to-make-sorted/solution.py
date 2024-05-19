class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        for i in range(len(strs[0])):
            ll=0
            for j in range(len(strs)-1):
                if(strs[j][i]>strs[j+1][i]):
                    ll+=1
            if(ll>0):
                c+=1
        return c                

        
