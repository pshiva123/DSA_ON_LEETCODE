class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        li=[]
        for i in range(len(nums)//2):
            k=min(nums)
            l=max(nums)
            avg=(k+l)/2
            avg=f"{avg:.1f}"
            avg=float(avg)
            li.append(avg)
            nums.remove(k)
            nums.remove(l)
        return min(li)
        
        
        
        
