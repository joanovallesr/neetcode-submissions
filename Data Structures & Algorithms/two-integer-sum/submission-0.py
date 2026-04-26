class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in nums and nums.index(diff) != i:
                ans.append(i)
                ans.append(nums.index(diff))
                return sorted(ans)
