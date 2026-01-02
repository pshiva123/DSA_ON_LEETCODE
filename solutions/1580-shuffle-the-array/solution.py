class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)
        i,j=0,n//2
        li=[]
        while i<n//2 and j<n:
            li.append(nums[i])
            li.append(nums[j])
            i+=1
            j+=1
        return li
