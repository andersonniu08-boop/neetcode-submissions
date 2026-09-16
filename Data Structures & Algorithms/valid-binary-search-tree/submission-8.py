# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node, maximum, minimum):
            if not node:
                return True

            if not (minimum < node.val < maximum):
                return False
            
            return dfs(node.left, min(maximum, node.val), minimum) and dfs(node.right, maximum, max(node.val, minimum))
            
        

        return dfs(root, float('inf'), float('-inf'))