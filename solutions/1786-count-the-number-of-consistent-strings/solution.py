class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
       s=set(allowed)
       #print(s)
       c=0
       for word in words:
        c1=0
        for i in range(len(word)):
            #print(word[i])
            if word[i] in s:
                c1+=1
            else:
                break
    
        if(c1==len(word)):
            c+=1
       return c

        
