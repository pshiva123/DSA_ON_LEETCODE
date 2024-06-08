class Solution:
    def clearDigits(self, s: str) -> str:
        li=[]
        for i in s:
            if(str.isdigit(i)):
                k=li.pop()
            else:
                li.append(i)
        return "".join(li)
        



            

            

               



        
