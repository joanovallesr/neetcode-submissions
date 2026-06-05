class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        for num in nums:
            currSum += num

            if currSum > maxSum:
                maxSum = currSum

            if currSum < 0:
                currSum = 0
        
        return maxSum