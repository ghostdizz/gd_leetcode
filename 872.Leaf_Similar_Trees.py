from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def __init__(self):
        self.string = ""
    def isLeafNode(self, node):
        if node == None: return False
        return node.left == None and node.right == None

    def stringLeafNode(self, node):
        if node == None:
            return                 
        self.stringLeafNode(node.left)
        self.stringLeafNode(node.right)
        if self.isLeafNode(node):
            self.string += str(node.val) + " "
        
        
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.stringLeafNode(root1)
        string1 = self.string
        self.string = ""
        self.stringLeafNode(root2)
        return string1 == self.string

