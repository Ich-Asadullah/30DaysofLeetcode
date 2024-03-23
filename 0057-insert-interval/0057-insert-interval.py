class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        out = []
        
        while i < len(intervals) and intervals[i][1] < newInterval[0] :
            out.append(intervals[i])
            
            i+=1
        
        while i < len(intervals) and intervals[i][0]<=newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1],intervals[i][1])] 
            i+=1
            
        out.append(newInterval)
        
        while i< len(intervals):
            out.append(intervals[i])
            i+=1
        
        return out