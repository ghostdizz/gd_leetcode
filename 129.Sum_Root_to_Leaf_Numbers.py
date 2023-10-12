from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.Sum = 0

    def ifLeafNode(self, node: Optional[TreeNode]) -> bool:
        if not node.left and not node.right: return True
        return False
    def Traversal(self, node: Optional[TreeNode], temp_sum: int) -> None:
        if not node: return None
        temp_sum = temp_sum*10 + node.val
        if self.ifLeafNode(node):
            self.Sum += temp_sum
            return None
        self.Traversal(node.left, temp_sum)
        self.Traversal(node.right, temp_sum)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.Traversal(root, 0)
        return self.Sum