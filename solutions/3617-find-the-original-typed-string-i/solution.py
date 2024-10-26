class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans=0
        i=0
        while i<len(word):
            c=1
            while i+1<len(word) and word[i]==word[i+1]:
                c+=1
                i+=1
            if c>1:
                ans+=c-1
            i+=1
        return ans+1
            
                
    
        
            
        
