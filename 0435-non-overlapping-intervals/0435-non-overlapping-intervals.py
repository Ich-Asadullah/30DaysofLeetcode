class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals.sort(key=lambda x:x[1])
        last = intervals[0][1]
        count = len(intervals)-1
        
        
        for i in range(1,len(intervals)):
            if intervals[i][0]>= last:
                count-=1
                last = intervals[i][1]
                
        return count
            
        