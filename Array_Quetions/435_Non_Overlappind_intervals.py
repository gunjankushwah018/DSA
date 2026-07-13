# first sort intervals
# create a variable previous_end to store the end of the previous interval
# create count variable to store the number of intervals to remove
# for every interval in intervals starting from the second interval:
#     if the end of the previous interval is greater than the start of the current interval:
#         increment count by 1
#         update previous_end to be the minimum of previous_end and the end of the current interval
#     else:
#         update previous_end to be the end of the current interval

# Time Complexity: O(nlogn) for sorting + O(n) for iterating through intervals = O(nlogn)
# Space Complexity: O(1) (in-place modification)





class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        previous_end=intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            if previous_end>intervals[i][0]:
                count+=1
                previous_end=min(previous_end,intervals[i][1])
            else:
                previous_end=intervals[i][1]
        return count