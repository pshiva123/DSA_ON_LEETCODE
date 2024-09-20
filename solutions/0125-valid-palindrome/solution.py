class Solution:
    def check(self,i,s):
        if i>=len(s)//2:
            return True
        if s[i]!=s[len(s)-i-1]:
            print(i)
            return False
        return self.check(i+1,s)
    def isPalindrome(self, s: str) -> bool:
        ss=""
        s=s.lower()
        for i in s:
            if 97<=ord(i)<=122 or 48<=ord(i)<=57:
                ss+=i
        print(ss)
        return self.check(0,ss)
        

        
