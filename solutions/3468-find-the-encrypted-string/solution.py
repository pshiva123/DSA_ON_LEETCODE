class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s1=""
        for i in range(len(s)):
            s1+=s[(i+k)%len(s)]
        return s1
        
