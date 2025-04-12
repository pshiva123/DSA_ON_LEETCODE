class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ss=sum(nums)%k
        return ss
        
