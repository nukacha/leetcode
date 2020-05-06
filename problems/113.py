from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        left, right = root.left, root.right
        if left is None and right is None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        else:
            new_sum = sum - root.val
            paths = list()
            left_paths = self.pathSum(left, new_sum)
            right_paths = self.pathSum(right, new_sum)
            if left_paths:
                paths.extend(self.update_path(left_paths, root.val))
            if right_paths:
                paths.extend(self.update_path(right_paths, root.val))
            return paths

    def update_path(self, paths, val):
        return [[val] + path for path in paths]
