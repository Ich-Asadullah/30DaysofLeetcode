class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x:x[0])
        
        res = [intervals[0]]
        
        for interval in intervals[1:]:
            if interval[0]>res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max( res[-1][1], interval[1])
        return res
        
                
        