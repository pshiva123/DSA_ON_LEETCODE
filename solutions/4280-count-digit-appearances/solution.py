class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        s=""
        for i in nums:
            s+=str(i)
        return s.count(str(digit))
        
