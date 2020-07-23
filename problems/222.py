class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        if lh == rh:    # left is full and right is complete
            return 2 ** lh + self.countNodes(root.right)
        else:    # left is complete and right is full
            return 2 ** rh + self.countNodes(root.left)
    
    def getHeight(self, root: TreeNode) -> int:
        h = 0
        while root:
            root = root.left
            h += 1
        return h
