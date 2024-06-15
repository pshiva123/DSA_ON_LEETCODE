class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence=list(map(str,sentence.split()))
        #print(sentence)
        ss=set(dictionary)
        #print(ss)
        for i in range(len(sentence)):
            s=""
            for j in range(0,len(sentence[i])):
                s+=sentence[i][j]
                #print(s)
                if s in ss:
                    sentence[i]=s
                    #print("this statement executed")
                    s=""
                    break
        stt=" ".join(sentence)
        return stt
                
            
            

        
