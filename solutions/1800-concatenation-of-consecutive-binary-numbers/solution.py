class Solution:
    MOD = 10**9 + 7

    li = [""] * (10**5 + 1)

    @staticmethod
    def help(n):
        return bin(n)[2:]

    for i in range(1, 10**5 + 1):
        li[i] = help(i)

    def concatenatedBinary(self, n: int) -> int:
        sol = 0
        current_power = 1   # represents 2^sendp % MOD

        for i in range(n, 0, -1):
            b = self.li[i]
            for bit in reversed(b):
                if bit == '1':
                    sol = (sol + current_power) % self.MOD
                current_power = (current_power * 2) % self.MOD

        return sol
