# sort intevals by start time and then by end time in descending order.
# Initialize a variable max_end to keep track of the maximum end time seen so far. 
# Iterate through the sorted intervals starting from the second interval.
# If the current interval's end time is less than or equal to max_end, it means the current interval is covered by a previous interval, so increment the count. 
# Otherwise, update max_end to the current interval's end time. 
# Finally, return the total number of intervals minus the count of covered intervals.

# Time Complexity: O(nlogn) for sorting + O(n) for iterating through intervals = O(nlogn)
# Space Complexity: O(1) (in-place modification)

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        count=0
        intervals.sort(key=lambda x: (x[0] , -x[1]))
        max_end=intervals[0][1]     
        for i in range(1,len(intervals)):
            if max_end>=intervals[i][1]:
                count+=1 
            else:
                max_end=intervals[i][1]
        return (len(intervals)-count)





        
