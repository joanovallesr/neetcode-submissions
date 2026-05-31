class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # i >> 1 is identical to i // 2
            # i & 1 isolates the last bit (0 if even, 1 if odd)
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp