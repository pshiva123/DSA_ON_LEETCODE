class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums)==1:
            return nums
        li=[nums[0],]
        n=len(nums)
        for i in range(1,n-1):
            flag=True
            for j in range(i):
                if nums[i]<=nums[j]:
                    flag=False
                    break
            if flag:
                li.append(nums[i])
                continue
            flag=True
            for j in range(i+1,n):
                if nums[i]<=nums[j]:
                    flag=False
                    break
            if flag:
                li.append(nums[i])
        li.append(nums[-1])
        return li
                
        
