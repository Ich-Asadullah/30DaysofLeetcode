class Solution(object):
    def isPalindrome(self, x):
        num = str(x)
        
        left =0
        right=len(num) -1
        
        while (right>left):
            if (num[left] != num[right]):
                return False
            right-=1
            left+=1
        return True
       
        