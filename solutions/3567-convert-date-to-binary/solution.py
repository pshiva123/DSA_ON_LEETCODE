class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y,m,d=map(int,date.split("-"))
        s=""
        k=bin(y)[2:]
        l=bin(m)[2:]
        n=bin(d)[2:]
        s+=k+"-"+l+"-"+n
        return s
       
              
