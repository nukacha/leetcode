from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        elif not (root.left or root.right):
            return [[root.val]]
        else:
            left = self.levelOrderBottom(root.left)
            right = self.levelOrderBottom(root.right)
            h = min(len(left), len(right))
            for i in range(-1, - h - 1, -1):
                left[i].extend(right[i])
            if len(left) < len(right):
                left = right[:-h if h != 0 else None] + left
            left.append([root.val])
            return left
