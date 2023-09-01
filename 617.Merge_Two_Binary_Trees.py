from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = TreeNode()
    def transform(self, root1, root2, root):
        if root1 == None and root2 == None: root = None 
        elif root1 == None: 
            root.val = root2.val
            if root2.left is not None:
                root.left = TreeNode()
                self.transform(None, root2.left, root.left)
            if root2.right is not None:
                root.right = TreeNode()
                self.transform(None, root2.right, root.right)
            return 
        elif root2 == None:
            root.val = root1.val
            if root1.left is not None:
                root.left = TreeNode()
                self.transform(root1.left, None, root.left)
            if root1.right is not None:
                root.right = TreeNode()
                self.transform(root1.right, None, root.right)
            return
        else:
            root.val = root1.val + root2.val
            if root1.left is not None or root2.left is not None:
                root.left = TreeNode()  
                self.transform(root1.left, root2.left, root.left)
            if root1.right is not None or root2.right is not None:
                root.right = TreeNode()
                self.transform(root1.right, root2.right, root.right)
            return 

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None: return None
        if root1 is None: return root2
        if root2 is None: return root1
        temp_root = self.root
        self.transform(root1, root2, temp_root)
        return self.root