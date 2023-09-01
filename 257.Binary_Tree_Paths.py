from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.lst = []

    def isLeafNode(self, node):
        if node is None: return False
        return node.left == None and node.right == None
    
    def findTreePaths(self, node, string):
        if node is None:
            return 
        
        if self.isLeafNode(node):
            string += str(node.val)
            self.lst.append(string)
        else:
            string += str(node.val) + "->"
            self.findTreePaths(node.left, string)
            self.findTreePaths(node.right, string)

    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.findTreePaths(root, "")
        return self.lst
    

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

print(Solution().binaryTreePaths(root))