class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        left = [1] * length
        right = [1] * length
        answer = [1] * length
        
        # Calculate the product of all elements to the left of each element
        for i in range(1, length):
            left[i] = left[i - 1] * nums[i - 1]
        
        # Calculate the product of all elements to the right of each element
        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        
        for i in range(length):
            answer[i] = left[i] * right[i]
        
        return answer
