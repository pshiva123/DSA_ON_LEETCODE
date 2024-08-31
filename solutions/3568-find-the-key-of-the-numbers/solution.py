class Solution:
    def gennum(self,num: int)->str:
        s=str(num)
        while(len(s)<4):
            s="0"+s
        return s 
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1=self.gennum(num1)
        num2=self.gennum(num2)
        num3=self.gennum(num3)
        print(num1,num2,num3)
        s=""
        for i in range(4):
            a,b,c=num1[i],num2[i],num3[i]
            a,b,c=int(a),int(b),int(c)
            k=min(a,b,c)
            k=str(k)
            s=s+k
        return int(s)    
        

        
