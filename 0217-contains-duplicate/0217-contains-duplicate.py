class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check_dict = {}
        
        for i in nums:
            if i in check_dict:
                return True
            else:
                check_dict[i] = 1
        
        return False