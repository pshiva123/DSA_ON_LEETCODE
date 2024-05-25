class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        c=0
        for word in words:
            l=len(word)
            if(s[:l]==word):
                c+=1
        return c
        
