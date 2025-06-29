class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        li=[]
        n=len(digits)
        carry=0
        t2=1+digits[-1]
        if t2>=10:
            carry=1
            t2=t2-10
        li.append(t2)

        for i in range(n-2,-1,-1):
            t=carry+digits[i]
            if t>=10:
                carry=1
                t=t-10
            else:
                carry=0
            li.append(t)
        if carry!=0:
            li.append(carry)
        return li[::-1]

        
