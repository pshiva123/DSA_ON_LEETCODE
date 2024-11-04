#from collections import Permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pointer=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                pointer=i
                break
        if pointer==-1:
            nums.sort()
        else:
            idx=pointer+1
            for i in range(pointer+2,len(nums)):
                if nums[i]>nums[pointer]:
                    if nums[i]<nums[idx]:
                        idx=i
            nums[idx],nums[pointer]=nums[pointer],nums[idx]
            nums[pointer+1:]=sorted(nums[pointer+1:])
                    





