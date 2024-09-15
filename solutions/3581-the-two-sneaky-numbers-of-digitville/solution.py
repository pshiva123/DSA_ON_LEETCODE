class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=set()
        li=[]
        for i in nums:
            if i in s:
                li.append(i)
            else:
                s.add(i)
        return li
