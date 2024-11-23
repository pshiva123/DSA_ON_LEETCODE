class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        li=[]
        n=len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                p1=j+1
                p2=n-1
                k=target-nums[i]-nums[j]
                while(p1<p2 and (p1<n and p2>j)):
                    ans=nums[p1]+nums[p2]
                    if ans==k:
                        temp=([nums[i],nums[j],nums[p1],nums[p2]])
                        if temp not in li:
                            li.append(temp)
                        p2-=1
                        p1+=1
                    elif ans>k:
                        p2-=1
                    else:
                        p1+=1
        return li
        
