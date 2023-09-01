from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        if root.left is None and root.right is None: return  str(root.val) 
        elif root.left is None: return str(root.val) + "()(" + self.tree2str(root.right) + ")" 
        elif root.right is None: return str(root.val) + "(" + self.tree2str(root.left) + ")"
        else: return str(root.val) + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"
