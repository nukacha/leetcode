class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        cand_set = set()
        def dfs(node):
            if node is None:
                return False
            elif node.val in cand_set:
                return True
            else:
                cand_set.add(k - node.val)
                return dfs(node.left) or dfs(node.right)
        return dfs(root)
