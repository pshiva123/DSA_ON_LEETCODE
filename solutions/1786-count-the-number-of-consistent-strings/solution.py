class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for word in words:
            k=len(word)
            l=0
            for i in word:
                if(allowed.find(i)!=-1):
                    l+=1
            if(l==k):
                c+=1
        return c                

        
