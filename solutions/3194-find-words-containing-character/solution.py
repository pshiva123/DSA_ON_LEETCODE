class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
         li=[]
         c=0
         for i in words:
            k=i.find(x)
            if(k!=-1):
                li.append(c)
            c+=1    
         return li 
        
