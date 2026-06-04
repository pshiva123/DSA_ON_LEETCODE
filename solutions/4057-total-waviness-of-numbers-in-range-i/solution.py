
li=[0]*(10**5+1)
for num in range(100,len(li)):
    s=str(num)
    n=len(s)
    cnt=0
    for i in range(1,n-1):
        if (int(s[i-1])>int(s[i]) and int(s[i+1])>int(s[i])) or  (int(s[i-1])<int(s[i]) and int(s[i+1])<int(s[i])):
            cnt+=1
    li[num]=cnt
prefixarr=[]
prefixarr.append(0)
for i in range(1,len(li)):
    prefixarr.append(prefixarr[-1]+li[i])
class Solution:

    def totalWaviness(self, num1: int, num2: int) -> int:
        return prefixarr[num2]-prefixarr[num1-1]
        
