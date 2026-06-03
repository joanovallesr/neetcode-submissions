class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0

        for i in range(len(nums) + 1):
            sum1 += i

        return sum1 - sum(nums)