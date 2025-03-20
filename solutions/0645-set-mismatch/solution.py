class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check=set(nums)
        temp=[i for i in range(1,len(nums)+1)]
        nums.extend(temp)
        xor=0
        for i in nums:
            xor^=i
        diff=xor  & -xor
        x=0
        y=0
        for i in nums:
            if i&diff:
                x^=i
            else:
                y^=i
        li=[]
        if x in check:
            li.append(x)
            li.append(y)
        else:
            li.append(y)
            li.append(x)
        return li
       
        

        
