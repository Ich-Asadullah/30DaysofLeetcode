class Solution(object):
    def singleNumber(self, nums):
        unique = 0;
        for num in nums:
            unique = unique^num
        return unique
        