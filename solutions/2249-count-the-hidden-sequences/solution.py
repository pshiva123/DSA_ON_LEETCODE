class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        min_prefix = 0
        max_prefix = 0
        
        for num in differences:
            prefix += num
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)
        
        valid_range = (upper - lower) - (max_prefix - min_prefix) + 1
        return max(0, valid_range)
        


