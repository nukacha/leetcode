from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def r(node, l_th, r_th):
            if node is None:
                return True
            if not (l_th < node.val < r_th):
                return False
            if not r(node.left, l_th, node.val):
                return False
            if not r(node.right, node.val, r_th):
                return False
            return True
        return r(root, -inf, inf)
