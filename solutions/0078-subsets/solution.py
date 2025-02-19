class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(nums,idx,n,li,temp):
            if idx==n:
                temp.append(li.copy())
                return
            li.append(nums[idx])
            sub(nums,idx+1,n,li,temp)
            li.pop()
            sub(nums,idx+1,n,li,temp)
        temp=[]
        li=[]
        sub(nums,0,len(nums),li,temp)
        return temp

        
