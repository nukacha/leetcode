from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        def f(s, t):
            if t < s:
                return None
            root_val = postorder.pop()
            if s == t:
                return TreeNode(inorder[s])
            root_idx = inorder.index(root_val)
            right = f(root_idx + 1, t)
            left = f(s, root_idx - 1)
            return TreeNode(root_val, left, right)
        return f(0, len(inorder) - 1)
