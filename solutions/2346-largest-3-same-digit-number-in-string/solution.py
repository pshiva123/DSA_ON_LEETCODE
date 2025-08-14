class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i=0
        n=len(num)
        largest=0
        flag=False
        while(i+3<=n):
            if len(set(num[i:i+3]))==1:
                flag=True
                if int(num[i:i+3])>largest:
                    largest=int(num[i:i+3])
            i+=1
        if not (flag):
            return ''
        return str(largest) if largest!=0 else '000'

        
