from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.dic = {}

    def average_of_level(self, node, level):
        if node is None: 
            if level not in self.dic:
                self.dic[level] = None
            return 
        else:
            if level not in self.dic: 
                self.dic[level] = [node.val]
            else:
                if self.dic[level] == None:
                    self.dic[level] = [node.val]
                else:
                    self.dic[level] += [node.val]
            self.average_of_level(node.left, level+1)
            self.average_of_level(node.right, level+1)  

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.dic[1] = [root.val]
        self.average_of_level(root, 1)
        lst = []
        for i in self.dic:
            if self.dic[i] is not None:
                lst.append(sum(self.dic[i])/(len(self.dic[i])))
       
        return lst