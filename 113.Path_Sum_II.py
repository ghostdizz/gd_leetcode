from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.list_ans = []

    def isLeafNode(self, node):
        return node.left is None and node.right is None
    
    def traversal(self, node, list_sum, targetSum):
        if node is not None:
            list_sum = list_sum + [node.val]
            if self.isLeafNode(node) and sum(list_sum) == targetSum:
                self.list_ans.append(list_sum)
            else:
                if node.left is not None:
                    self.traversal(node.left, list_sum, targetSum)
                if node.right is not None:
                    self.traversal(node.right, list_sum, targetSum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.traversal(root, [], targetSum)
        return self.list_ans
