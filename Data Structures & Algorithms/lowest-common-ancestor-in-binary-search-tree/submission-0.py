# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root):
            #we want to find when min(q, p) is less than root.left and max is more than root.right
            
            if root.val >= min(p.val, q.val) and root.val <= max(p.val, q.val):
                return root
            if root.val > min(p.val, q.val) and root.val > max(p.val, q.val):
                return dfs(root.left)
            else:
                return dfs(root.right)
        
        return dfs(root)
            
            

            
            