class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are empty -> identical
        if not p and not q:
            return True

        # One is empty, or values don't match -> not identical
        if not p or not q or p.val != q.val:
            return False

        # Check left subtrees together AND right subtrees together
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)