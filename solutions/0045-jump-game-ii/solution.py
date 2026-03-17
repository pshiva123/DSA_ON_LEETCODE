class Solution:
    def jump(self, nums: List[int]) -> int:
        c=0
        end=0 #before step 1
        uptoindex=0
        for i in range(len(nums)-1):
            uptoindex=max(uptoindex,i+nums[i])
            if i==end:
                #if reached a index that we treatad as a end before
                c+=1
                end=uptoindex
        return c
        


