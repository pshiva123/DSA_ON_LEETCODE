class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        ans=''
        i=0
        while(i<len(s)):
            if s[i]=='6':
                ans+='9'
                i+=1
                break
            else:
                ans+=s[i]
                i+=1
        return int(ans+s[i:])


        
