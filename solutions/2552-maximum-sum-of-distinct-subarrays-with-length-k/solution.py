class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hash={}
        s=0
        for i in range(k):
            if nums[i] not in hash:
                hash[nums[i]]=1
            else:
                hash[nums[i]]+=1
            s+=nums[i]
        maxi=0
        if len(hash)==k:
            maxi=max(maxi,s)
        
        for i in range(k,len(nums)):
            if hash[nums[i-k]]>1:
                hash[nums[i-k]]-=1
            else:
                hash.pop(nums[i-k])
            s-=nums[i-k]
            if nums[i] not in hash:
                hash[nums[i]]=1
            else:
                hash[nums[i]]+=1
            s+=nums[i]
            if len(hash)==k:
                maxi=max(maxi,s)
        return maxi
            

        
