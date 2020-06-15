from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leaf_sequence(root1) == self.leaf_sequence(root2)
        
    def leaf_sequence(self, root: TreeNode) -> List[int]:
        stack = [root]
        seq = []
        while stack:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            if node.left is None and node.right is None:
                seq.append(node.val)
        return seq
