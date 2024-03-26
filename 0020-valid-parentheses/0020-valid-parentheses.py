class Solution(object):
    def isValid(self, s):
        bracket_map = {')': '(', '}': '{', ']': '['}
        open_brackets = ['(', '{', '[']
        stack = [] 

        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif char in bracket_map:
                if not stack or bracket_map[char] != stack.pop():
                    return False
            else:
                return False
        return not stack
        