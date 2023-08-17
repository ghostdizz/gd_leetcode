from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isSame(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        elif root1.val != root2.val:
            return False
        return True and self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)
    
    def flipTree(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return 0
        root.left, root.right = root.right, root.left
        self.flipTree(root.left)
        self.flipTree(root.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.flipTree(root.right)
        return self.isSame(root.left, root.right)
    