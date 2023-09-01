from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convert(self, node):
        if node == None:
            return 
        temp_node = node
        temp_node_right = temp_node.right
        temp_node.right = temp_node.left
        temp_node.left = temp_node_right
        self.convert(temp_node.left)
        self.convert(temp_node.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.convert(root)
        return root
