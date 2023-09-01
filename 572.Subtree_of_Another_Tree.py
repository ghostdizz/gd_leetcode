from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.boolean = False

    def theSameTree(self, root1, root2):
        if root1 == None and root2 == None: return True
        if root1 == None or root2 == None: return False
        if root1.val != root2.val: return False
        return True and self.theSameTree(root1.left, root2.left) and self.theSameTree(root1.right, root2.right)
    
    def checkSameTree(self, root1, root2):
        if not root1: return
        if self.theSameTree(root1, root2):
            self.boolean = True
            return
        if not self.boolean:
            self.checkSameTree(root1.left, root2)
            self.checkSameTree(root1.right, root2)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.checkSameTree(root, subRoot)
        return self.boolean