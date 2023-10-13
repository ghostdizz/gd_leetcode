from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.lst = []
    def traversal(self, node):
        if node == None: return None
        self.lst.append(node.val)
        self.traversal(node.left)
        self.traversal(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traversal(root)
        self.lst.sort()
        return self.lst[k-1]