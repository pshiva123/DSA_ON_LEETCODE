class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        st=""
        for word in words:
            if(word==word[::-1]):
                st=word
                return st
        return st        
        
