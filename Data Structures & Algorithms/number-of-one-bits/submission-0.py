class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # erase the lower set bit
            n &= (n - 1)
            # increment count for each erased bit
            count += 1
        
        return count