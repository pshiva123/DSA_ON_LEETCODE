class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        nums.sort()
        c=0
        k=0
        print(nums)
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                continue
            if(nums[i]+1==nums[i+1]):
                c+=1
            else:
                k=max(c+1,k)
                c=0
        return max(k,c+1)

                        
