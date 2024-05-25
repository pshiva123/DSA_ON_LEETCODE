class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        x=0
        s=set()
        for i in nums:
            if(nums.count(i)==2):
                s.add(i)
        for i in s:
            x=x^i
        return x
        
