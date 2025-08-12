class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        # Precompute powers <= n
        powers = []
        i = 1
        while i**x <= n:
            powers.append(i**x)
            i += 1
        
        # 1D DP: dp[s] = number of ways to get sum s
        dp = [0] * (n + 1)
        dp[0] = 1  # base case: one way to make sum 0
        
        for p in powers:
            for s in range(n, p - 1, -1):  # reverse to avoid reusing numbers
                dp[s] = (dp[s] + dp[s - p]) % MOD
        
        return dp[n]

