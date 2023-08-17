from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if abs(self.max_depth(root.left) - self.max_depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
