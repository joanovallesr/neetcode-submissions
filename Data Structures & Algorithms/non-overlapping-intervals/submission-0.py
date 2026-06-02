class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # sort strictly by the end number
        intervals.sort(key=lambda x: x[1])

        # keep track of the end time on the last accepted interval
        endPoint = intervals[0][1]
        removals = 0

        # iterate through the rest of the intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] < endPoint:
                removals += 1
            else:
                endPoint = intervals[i][1]

        return removals