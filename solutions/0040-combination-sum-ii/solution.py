class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def cs(nums,hash,s,li,idx,n,target):
            if s==target:
                hash.append(li.copy())        
                return
            for i in range(idx,n):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                if s+nums[i]>target:
                    break
                li.append(nums[i])
                cs(nums,hash,s+nums[i],li,i+1,n,target)
                li.pop()  
        hash=[]
        li=[]
        candidates.sort()
        #print(candidates)
        cs(candidates,hash,0,li,0,len(candidates),target)
        return hash
