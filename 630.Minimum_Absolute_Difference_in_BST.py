from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getList(self, node):
        if node:
            return [node.val] + self.getList(node.left) + self.getList(node.right)
        return []
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = self.getList(root)
        lst = sorted(list(set(lst)))
        minimum = lst[1] - lst[0]
        for i in range(len(lst)-1):
            if lst[i+1] - lst[i] < minimum:
                minimum = lst[i+1] - lst[i]
        return minimum

