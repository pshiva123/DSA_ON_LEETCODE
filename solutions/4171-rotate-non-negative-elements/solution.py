class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        li=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                li.append(nums[i])
        if len(li)==0:
            return nums
        k=k%(len(li))
        li=li[k:]+li[:k]
        idx=0
        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i]=li[idx]
                idx+=1
        return nums
        
        
