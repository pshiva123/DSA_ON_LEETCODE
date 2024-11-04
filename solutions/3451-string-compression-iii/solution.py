class Solution:
    def compressedString(self, word: str) -> str:
        s=""
        c=1
        for i in range(1,len(word)):
            if word[i]==word[i-1]:
                if c==9:
                    s+=str(c)
                    s+=word[i-1]
                    c=0
                c+=1
            else:
                s+=str(c)
                s+=word[i-1]
                c=1
        s+=str(c)
        s+=word[-1]
        return s
        


        
