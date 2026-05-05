class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        finalList = []

        def backtrack(currPath, currList, sum1):
            if sum1 == target:
                finalList.append(currPath)
                return
            elif sum1 > target:
                return
            else:
                for i in range(len(currList)):
                    sum1 += currList[i]
                    backtrack(currPath + [currList[i]], currList[i:], sum1)
                    sum1 -= currList[i]
        backtrack([], nums, 0)
        return finalList