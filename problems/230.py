class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.i = 0
        self.ith_val = 0
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root.left is not None and self.i < k:
            self.kthSmallest(root.left, k)
        if self.i < k:
            self.i += 1
            self.ith_val = root.val
        if root.right is not None and self.i < k:
            self.kthSmallest(root.right, k)
        return self.ith_val
