class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            num=i
            num=bin(num)[2:]
            if num.count("1")==k:
                c+=nums[i]
        return c

        
