class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        left, right = root.left, root.right
        if left is None and right is None:
            if root.val == sum:
                return True
            else:
                return False
        else:
            new_sum = sum - root.val
            return (
                self.hasPathSum(left, new_sum)
                or self.hasPathSum(right, new_sum)
            )
