class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for n in nums:
            if n-1 not in nums:
                length = 1
                nxt = n + 1

                while nxt in nums:
                    length += 1
                    nxt += 1
                
                best = max(best, length)

        return best