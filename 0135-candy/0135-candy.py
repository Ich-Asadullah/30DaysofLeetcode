class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        result_arr = [1] * (len(ratings))
        result = 0
        
        for i in range(1, len(ratings)):
            if(ratings[i]>ratings[i-1]):
                if(result_arr[i]<=result_arr[i-1]):
                    result_arr[i] = result_arr[i-1]+1
        
        for i in range(len(ratings)-2, -1, -1):
            if(ratings[i]>ratings[i+1]):
                if(result_arr[i]<=result_arr[i+1]):
                    result_arr[i] = result_arr[i+1]+1
        
        for i in result_arr:
            result+=i
        
        return result