# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        level = [root]
        
        while level and root:
            ans.append(node.val for node in level)
            
            temp = []
            for i in level:
                temp.extend([i.left, i.right])
            
            level = [leaf for leaf in temp if leaf]
        
        return ans
        