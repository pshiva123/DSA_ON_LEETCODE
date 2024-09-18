class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        one=0
        two=0
        for i in nums:
            if i==1:
                one+=1
            elif i==2:
                two+=1
            else:
                zero+=1
        for i in range(zero):
            nums[i]=0
        for i in range(zero,zero+one):
            nums[i]=1
        for i in range(zero+one,zero+one+two):
            nums[i]=2
            

        
