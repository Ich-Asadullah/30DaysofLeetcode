class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max, min, dif= 0, 0, 0

        for i in range (len(prices)):
            if i==0:
                min=prices[i]
            elif prices[i]>min and prices[i]>max:
                max=prices[i]
            elif prices[i]<min:
                min = prices[i]
                max=0
            if dif<=(max-min):
                    dif= (max-min)
        if dif<=0:
            return 0
        else:
            return (dif)
            