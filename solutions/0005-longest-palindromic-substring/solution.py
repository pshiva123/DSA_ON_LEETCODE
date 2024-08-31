class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp=""
        if(len(s)==1):
            return s
        for i in range(len(s)-1):
            for j in range(i,len(s)):
                st=s[i:j+1]
                if(st==st[::-1] and len(st)>len(temp)):
                    temp=st
        return temp

