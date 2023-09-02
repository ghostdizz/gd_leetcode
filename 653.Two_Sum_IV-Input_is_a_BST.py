from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.dic = {}
        self.boolean = False
    def find(self, node, k):
        if node is None: return 
        if (k-node.val) in self.dic:
            self.boolean = True
            return
        else:
            self.dic[node.val] = True
        self.find(node.left, k)
        self.find(node.right, k)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.find(root, k)
        return self.boolean