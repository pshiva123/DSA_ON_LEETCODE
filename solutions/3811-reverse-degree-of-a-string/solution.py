class Solution:
    def reverseDegree(self, s: str) -> int:
        li=[i for i in range(26,0,-1)]
        x=0
        for i in range(len(s)):
            ascii=ord(s[i])-97
            x+=(i+1)*li[ascii]
        return x
        
