from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    lst = []
    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            self.lst += [node.val]
            self.inorder(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.lst = []
        self.inorder(root)
        return self.lst