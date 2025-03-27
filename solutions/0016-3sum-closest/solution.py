class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mini=float('inf')
        nums.sort()
        n=len(nums)
        ans=-1
        for i in range(n):
            j=i+1
            k=n-1
            find=target-nums[i]
            while(j<k):
                temp=nums[i]+nums[j]+nums[k]
                if abs(target-temp)<mini:
                    ans=temp
                    mini=abs(target-temp)
                if nums[j]+nums[k]<find:
                    j+=1
                elif nums[j]+nums[k]==find:
                    ans=temp
                    break
                else:
                    k-=1
        return ans
        
