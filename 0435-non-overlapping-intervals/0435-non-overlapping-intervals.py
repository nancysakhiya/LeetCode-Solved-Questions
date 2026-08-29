class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        cnt = 0
        prevend = intervals[0][1]

        for i in range(1, n):

            # if overlap we remove the interval which ends late. 
            if intervals[i][0] < prevend:
                cnt += 1
                prevend = min(intervals[i][1], prevend)

            # No overlap  
            else:
                prevend = intervals[i][1]

        return cnt