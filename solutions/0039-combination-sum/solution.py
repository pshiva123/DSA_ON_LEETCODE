class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def cs(nums,temp,s,li,idx,n,target):
            if n==idx:
                if s==target:
                    temp.append(li.copy())
                return
            if (nums[idx]+s<=target):
                li.append(nums[idx])
                cs(nums,temp,s+nums[idx],li,idx,n,target)
                li.pop()
            cs(nums,temp,s,li,idx+1,n,target)
        temp=[]
        li=[]
        cs(candidates,temp,0,li,0,len(candidates),target)
        return temp
