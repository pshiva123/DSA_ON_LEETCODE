class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        st=set('aeiou')
        n=len(s)
        i=n-1
        while i>=0 and s[i] in st:
            i-=1
        return s[:i+1]
        
