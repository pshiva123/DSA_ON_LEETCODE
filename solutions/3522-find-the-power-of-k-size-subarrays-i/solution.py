class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        li=[]
        n=len(nums)
        for i in range(n-k+1):
            c=0
            for j in range(i,i+k-1):
                if nums[j]>=nums[j+1] or nums[j]+1!=nums[j+1]:
                    c=1
                    break
            if c==1:
                li.append(-1)
            else:
                li.append(nums[i+k-1])
        return li
