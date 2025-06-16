from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        """
        Partition nums (length = 2n) into two groups of size n to minimize
        |sum(group1) - sum(group2)|.
        """

        n = len(nums) // 2
        total = sum(nums)
        half = total // 2

        # Generate all (subset-size → list of subset-sums) for one half
        def gen_sums(arr):
            m = len(arr)
            sums = [[] for _ in range(m+1)]
            # iterate all bitmasks of arr
            for mask in range(1 << m):
                s = 0
                cnt = 0
                for i in range(m):
                    if mask & (1 << i):
                        s += arr[i]
                        cnt += 1
                sums[cnt].append(s)
            return sums

        left, right = nums[:n], nums[n:]
        left_sums  = gen_sums(left)
        right_sums = gen_sums(right)

        # sort each list in right_sums for binary search
        for lst in right_sums:
            lst.sort()

        best = float('inf')

        # For each possible size k taken from left half,
        # we take (n-k) from right. We want s_left + s_right
        # as close as possible to half = total//2
        for k in range(n+1):
            A = left_sums[k]
            B = right_sums[n-k]
            B.sort()
            for s in A:
                # target is half - s
                tgt = half - s
                # find in B closest to tgt
                i = bisect_left(B, tgt)
                # check B[i]
                if i < len(B):
                    cur = abs((s + B[i]) * 2 - total)
                    if cur < best:
                        best = cur
                # check B[i-1]
                if i > 0:
                    cur = abs((s + B[i-1]) * 2 - total)
                    if cur < best:
                        best = cur

        return best

