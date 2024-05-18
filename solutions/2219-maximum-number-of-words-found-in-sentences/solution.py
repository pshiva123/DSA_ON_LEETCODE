class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=0
        for sentence in sentences:
            words=1
            for i in sentence:
                if(i==" "):
                    words+=1
            if(words>l):
                l=words
        return l                   

        
