class Solution:
    def minimumSum(self, num: int) -> int:
        s=str(num)
        s=sorted(s)
        num1=""
        num2=""
        i=0
        while(i<len(s)):
            num1+=s[i]
            i+=2
        j=1
        while(j<len(s)):
            num2+=s[j]
            j+=2
        num1=int(num1)
        num2=int(num2)
        return num1+num2
        
