from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        level = [root]
        l2r = False     # left to right
        while level := [x for x in level if x is not None]:
            new_level = []
            result.append([x.val for x in level])
            for node in reversed(level):
                if node is None:
                    continue
                children = node.left, node.right
                new_level.extend(children if l2r else children[::-1])
            l2r = not l2r
            level = new_level
        return result
