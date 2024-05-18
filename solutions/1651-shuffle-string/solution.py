class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        li=[0]*len(s)
        k=0
        for i in indices:
            li[i]=s[k]
            k=k+1
        ss=""    
        for i in li:
            ss=ss+i    
        return ss    
