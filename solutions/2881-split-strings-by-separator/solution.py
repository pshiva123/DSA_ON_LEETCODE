class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        li=[]
        for word in words:
            li1=[]
            li1=list(word.split(separator))
            for i in li1:
                if(len(i)!=0):
                    li.append(i)
        return li
        
        
