from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left == None and root.right == None:
            return True
        elif root.left == None:
            if root.val != root.right.val:
                return False
        elif root.right == None:
            if root.val != root.left.val:
                return False
        elif root.val != root.left.val or root.val != root.right.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
    