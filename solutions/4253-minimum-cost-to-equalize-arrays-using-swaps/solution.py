from collections import Counter
class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort()
        if nums1==nums2:
            return 0
        d1=Counter(nums1)
        d2=Counter(nums2)
        ans=0
        for num in d1:
            if num in d2:
                x=d1[num]
                while x>0 and d2[num]>0:
                    x-=1
                    d1[num]-=1
                    d2[num]-=1
                if d2[num]==0:
                    d2.pop(num)
       
        if sum(d1.values())!=sum(d2.values()):
            return -1
        for num in d1:
            if d1[num]%2!=0:
                return -1
            else:
                ans+=d1[num]//2
        for num in d2:
            if d2[num]%2!=0:
                return -1
            else:
                ans+=d2[num]//2
        
                
        return ans//2
        

        
        
            
        
