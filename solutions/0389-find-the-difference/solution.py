class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sol1,sol2=0,0
        for i in s:
            sol1+=ord(i)
        for i in t:
            sol2+=ord(i)
        return chr(sol2-sol1)
        
