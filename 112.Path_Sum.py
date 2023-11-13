from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isLeafNode(self, node: Optional[TreeNode]) -> bool:
        if node.right is None and node.left is None:
            return True
        return False


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        elif root.val == targetSum and self.isLeafNode(root):
            return True
        else:
            return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        