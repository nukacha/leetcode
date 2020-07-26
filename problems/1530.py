from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        nodes = [root]
        depth = 0
        r = [0]
        def dfs(node):
            if node is None:
                return Counter()
            if node.left is None and node.right is None:
                return Counter([0])
            left = dfs(node.left)
            right = dfs(node.right)
            for ld in left:
                for rd in right:
                    if rd + ld + 1 < distance:
                        r[0] += left[ld] * right[rd]
            cnt = Counter()
            for k, v in sum([left, right], Counter()).items():
                cnt[k + 1] = v
            return cnt
        dfs(root)
        return r[0]
