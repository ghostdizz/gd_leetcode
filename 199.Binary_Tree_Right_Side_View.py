from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.idx = 0
        self.max_depth = 0
        self.lst = []
    
    def isLeafNode(self, node):
        if not node: return False
        if not node.right and not node.left: return True
        return False
    
    def recursion(self, node, idx):
        if node is None: return 
        
        if idx > self.idx:
            self.lst.append(node.val)
            self.idx = idx
        if self.max_depth < self.idx:
            self.max_depth = self.idx
        self.recursion(node.right, idx+1)
        self.recursion(node.left, idx+1)
        



    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        if self.isLeafNode(root): return [root.val]
        self.recursion(root, 1)
        return self.lst
    
