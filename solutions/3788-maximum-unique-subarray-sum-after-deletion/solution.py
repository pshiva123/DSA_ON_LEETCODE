class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=set(nums)
        t=set()
        for num in s:
            if num>0 and num<=100:
                t.add(num)
        return sum(t) if t else max(nums)


        
