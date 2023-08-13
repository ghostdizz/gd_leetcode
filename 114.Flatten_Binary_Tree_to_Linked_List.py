from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current_node = root
        while current_node:
            if current_node.left != None:
                prev_node = current_node.left
                while prev_node.right:
                    prev_node = prev_node.right
                prev_node.right = current_node.right
                current_node.right = current_node.left
                current_node.left = None
            current_node = current_node.right
        

