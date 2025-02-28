class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]>5:
            return False
        five=1
        ten=0
        for i in range(1,len(bills)):
            if bills[i]==5:
                five+=1
            if bills[i]==10:
                if five<=0:
                    return False
                five-=1
                ten+=1
            elif bills[i]==20:
                if ten<=0 and five>=3:
                    five-=3
                elif ten>0 and five>0:
                    ten-=1
                    five-=1
                else:
                    return False
        return True


        
