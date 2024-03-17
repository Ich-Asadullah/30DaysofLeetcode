class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1,1])
            else:
                new_add = []
                
                for j in range(len(result[-1]) +1):
                    if j in (0, len(result[-1])):
                        new_add.append(1)
                    else:
                        new_add.append(result[-1][j-1] + result[-1][j])
                result.append(new_add)
        return result