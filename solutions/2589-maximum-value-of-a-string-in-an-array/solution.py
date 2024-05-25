class Solution:
    def alphanum(self,word :str)->bool:
        for i in word:
            if((i.isalpha())):
                return True
        return False    
    def maximumValue(self, strs: List[str]) -> int:
        value=0
        for st in strs:
            if(self.alphanum(st)):
                k=len(st)
            else:
                k=int(st)
            value=max(value,k)
        return value        

        
