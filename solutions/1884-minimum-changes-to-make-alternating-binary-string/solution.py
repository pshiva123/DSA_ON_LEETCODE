class Solution:
    def minOperations(self, s: str) -> int:
        c=0
        n=len(s)
        prev=s[0]
        for i in range(1,n):
            if s[i]!=prev:
                prev=s[i]
            else:
                prev=str(int(s[i])^1)
                c+=1
        c2=1
        prev=str(int(s[0])^1)
        for i in range(1,n):
            if prev!=s[i]:
                prev=s[i]
            else:
                prev=str(int(s[i])^1)
                c2+=1
        print(c,c2)
        return min(c,c2)
        

        
