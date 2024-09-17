class Solution:
    def reverseWords(self, s: str) -> str:
        li=list(map(str,s.split()))
        s=""
        for i in range(len(li)-1,-1,-1):
            if i==0:
                s+=li[i]
            else:
                s+=li[i]+" "
        return s
        
