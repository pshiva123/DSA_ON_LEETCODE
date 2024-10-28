class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=0
        negitive=1
        li=[0]*len(nums)
        for i in nums:
            if i>0:
                li[positive]=i
                positive+=2
            else:
                li[negitive]=i
                negitive+=2
        return li



        
