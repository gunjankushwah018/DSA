# first sort intervals
# create result list and store first interval in it
# for each interval in intervals starting from second interval:
#     if the end of the last interval in result is greater than or equal to the start of the current interval:
#         merge the two intervals by taking the minimum start and maximum end
#         update the last interval in result with the merged interval
#     else:
#         append the current interval to result
#  time complexity: O(nlogn) for sorting + O(n) for merging = O(nlogn)
#  space complexity: O(n) for the result list
    


class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            if result[-1][1]>=intervals[i][0]:
                merge=[min(result[-1][0],intervals[i][0]),max(result[-1][1],intervals[i][1])]
                result[-1]=merge
            else:
                result.append(intervals[i])
        return result        