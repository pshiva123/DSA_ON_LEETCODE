class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        set1=set(['a','e','i','o','u'])
        ans=0
        for j in range(k):
            if s[j] in set1:
                ans+=1      
        i=k
        j=0
        prev=ans
        while(i<len(s)):
            temp=prev
            print(temp,s[j],s[i])
            if s[j] in set1:
                temp-=1
            if s[i] in  set1:
                temp+=1
            prev=temp
            ans=max(ans,temp)
            print(ans)
            i+=1
            j+=1
        return ans


        
