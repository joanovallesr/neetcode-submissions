class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # shift the result left to make room for the incoming bit
            result <<= 1
            # isolate the rightmost bit of n and add it to the result
            result |= (n & 1)
            # shift n right to move onto the next bit
            n >>= 1

        return result