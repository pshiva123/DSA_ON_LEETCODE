class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Edge case: if Alice never draws OR if she can never exceed n
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0  # start with 0 points
        windowSum = 1.0  # sliding window sum
        result = 0.0

        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts

            if i < k:  
                # Alice can still draw from this state
                windowSum += dp[i]
            else:
                # Alice stops, add to final result
                result += dp[i]

            # Maintain sliding window of size maxPts
            if i - maxPts >= 0:
                windowSum -= dp[i - maxPts]

        return result

