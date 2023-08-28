class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def __init__(self):
        self.head = TreeNode()
        self.temp_head = self.head
    
    def traversal(self, node):
        if node is not None:
            self.traversal(node.left)
            self.temp_head.right = TreeNode(node.val)
            self.temp_head = self.temp_head.right
            self.traversal(node.right)
        
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.traversal(root)
        return self.head.right
        