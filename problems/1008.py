from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        return TreeNode(
            preorder[0],
            self.bstFromPreorder([v for v in preorder if v < preorder[0]]),
            self.bstFromPreorder([v for v in preorder if v > preorder[0]])
        )
