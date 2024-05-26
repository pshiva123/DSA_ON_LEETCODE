class Solution:
    def compressedString(self, word: str) -> str:
        if(len(word)==1):
            return "1"+word[0]
        elif(len(word)==0):
            return "0"
        else:
            st=""
            c=1
            for i in range(0,len(word)-1):
                if(c==9):
                    k=str(c)
                    st=st+k
                    st=st+word[i]
                    c=1
                    continue
                if(word[i]==word[i+1]):
                    c+=1
                else:
                    k=str(c)
                    st=st+k
                    st=st+word[i]
                    c=1
            if(word[-1]==word[-2]):
                k=str(c)
                st=st+k
                st=st+word[-1]
            else:
                st=st+"1"
                st=st+word[-1]
        return st
            
        
