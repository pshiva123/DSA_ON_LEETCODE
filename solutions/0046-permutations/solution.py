from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        li=list(permutations(nums))
        return li

        
