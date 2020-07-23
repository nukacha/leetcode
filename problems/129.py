class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(node, path=[]):
            if node is None:
                return 0
            path = path.copy()
            path.append(node.val)
            if node.left is None and node.right is None:
                return int(''.join(map(str, path)))
            return dfs(node.left, path) + dfs(node.right, path)
        return dfs(root)
