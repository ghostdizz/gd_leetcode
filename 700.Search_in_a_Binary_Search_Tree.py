from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def search(self, node, val):
        if node is not None:
            if node.val == val:
                return node
            if node.val < val:
                return self.search(node.right, val)
            else:
                return self.search(node.left, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root, val)