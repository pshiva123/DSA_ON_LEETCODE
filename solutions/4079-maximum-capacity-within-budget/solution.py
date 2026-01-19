from bisect import bisect_left
from typing import List

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        machines = sorted(zip(costs, capacity))   # sort by cost
        n = len(machines)
        costs_s = [c for c,_ in machines]
        caps_s  = [cap for _,cap in machines]

        # best single machine
        ans = 0
        for c, cap in machines:
            if c < budget:
                ans = max(ans, cap)

        # prefix max capacities (best capacity among indices 0..i)
        prefix = [0] * n
        prefix[0] = caps_s[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], caps_s[i])

        # consider each machine as the "right" machine in pair (left index < i)
        for i in range(n):
            # want left_cost < budget - costs_s[i]
            limit = budget - costs_s[i]
            # bisect_left gives first index with cost >= limit,
            # so eligible left indices are [0 .. pos-1]
            pos = bisect_left(costs_s, limit)
            # we must only use left indices strictly less than i
            pos = min(pos, i)
            if pos - 1 >= 0:
                ans = max(ans, caps_s[i] + prefix[pos - 1])

        return ans

