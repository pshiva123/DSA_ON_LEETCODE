class Solution:
    def romanToInt(self, s: str) -> int:
        numbers={'I':1,'V':5,'X':10,'L':50 ,'C':100,'D':500,'M':1000}
        su=0
        n=len(s)
        for i in range(n-1):
            if s[i]=='I' and s[i+1]=='V':
                su-=1
            elif s[i]=='I' and s[i+1]=='X':
                su-=1
            elif s[i]=='X' and s[i+1]=='L':
                su-=10
            elif s[i]=='X' and s[i+1]=='C':
                #print(i,"en",su)
                su-=10
                #print(i,su)
            elif s[i]=='C' and s[i+1]=='D':
                su-=100
            elif s[i]=='C' and s[i+1]=='M':
                su-=100
            else:
                su+=numbers[s[i]]
            #print(i,su)
        return su+numbers[s[-1]]
            
            


