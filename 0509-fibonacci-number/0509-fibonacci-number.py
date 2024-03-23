class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fibb(n):
            if n <=1:
                return n
            else:
                return fibb(n-1) + fibb(n-2)
        
        return fibb(n)
