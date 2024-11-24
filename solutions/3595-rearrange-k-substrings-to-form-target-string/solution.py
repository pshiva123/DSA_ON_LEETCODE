class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n=len(s)
        ss=n//k
        i=0
        li=[]
        while(i<n):
            li.append(s[i:ss+i])
            i+=ss
        i=0
        l2=[]
        while(i<n):
            l2.append(t[i:ss+i])
            i+=ss
        li.sort()
        l2.sort()
        return li==l2
            
        
