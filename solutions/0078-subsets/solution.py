class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        cur=[]
        f(nums,0,cur,arr)
        return arr
def f(nums,idx,cur,arr):
    if idx==len(nums):
        arr.append(cur)
        return 
    f(nums,idx+1,cur+[nums[idx]],arr)
    f(nums,idx+1,cur,arr)
