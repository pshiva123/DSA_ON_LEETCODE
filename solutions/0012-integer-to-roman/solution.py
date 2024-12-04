class Solution:
    def intToRoman(self, num: int) -> str:
        values=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),
        (40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        s=""
        for key,value in values:
            if num>0:
                count=num//key
                s+=value*count
                num=num%key
            else:
                break
        return s        
