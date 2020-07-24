class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        l_stack = [root.left]
        r_stack = [root.right]
        while l_stack:
            l = l_stack.pop()
            r = r_stack.pop()
            if l is None and r is None:
                continue
            elif (l is None or r is None) or l.val != r.val:
                return False
            l_stack.extend([l.left, l.right])
            r_stack.extend([r.right, r.left])
        return True
