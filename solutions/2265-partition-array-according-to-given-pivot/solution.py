class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        matched=[]
        for val in nums:
            if val<pivot:
                left.append(val)
            elif val==pivot:
                matched.append(val)
            else:
                right.append(val)
        idx=0
        for val in left:
            nums[idx]=val
            idx+=1
        for val in matched:
            nums[idx]=val
            idx+=1
        for val in right:
            nums[idx]=val
            idx+=1
        return nums
        
