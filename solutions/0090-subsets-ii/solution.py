class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        li=[]
        def solve(idx,n,li,temp,nums):
            temp.append(li.copy())
            for i in range(idx,n):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                li.append(nums[i])
                solve(i+1,n,li,temp,nums)
                li.pop()
        nums.sort()
        solve(0,len(nums),li,temp,nums)
        return temp
        
