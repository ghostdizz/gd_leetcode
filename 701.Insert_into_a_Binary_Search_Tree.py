from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp_node = root
        if root is None:
            return TreeNode(val)
        while temp_node != None:
            if temp_node.val < val:
                if temp_node.right is None:
                    temp_node.right = TreeNode(val)
                    break
                else:
                    temp_node = temp_node.right
            elif temp_node.val > val:
                if temp_node.left is None:
                    temp_node.left = TreeNode(val)
                    break
                else:
                    temp_node = temp_node.left
        return root
