class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf(node: TreeNode) -> bool:
    if node is None:
        return False
    else:
        return node.left is None and node.right is None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif is_leaf(root.left):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return sum(map(self.sumOfLeftLeaves, (root.left, root.right)))
