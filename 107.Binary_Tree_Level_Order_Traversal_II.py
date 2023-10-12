from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = []
        self.length = 0

    def traversal(self, node, level):
        if not node: return 0
        if level >= self.length:
            self.ans.append([node.val])
            self.length += 1
        else:
            self.ans[level].append(node.val)

        self.traversal(node.left, level+1)
        self.traversal(node.right, level+1)

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traversal(root, 0)
        return self.ans[::-1]

