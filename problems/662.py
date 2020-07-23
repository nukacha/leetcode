class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        nodes = [(root, 0)]
        width = 1
        while nodes:
            next_nodes = []
            most_left = float('inf')
            most_right = -float('inf')
            for node, i in nodes:
                for j, child in enumerate([node.left, node.right]):
                    if child is None:
                        continue
                    k = i * 2 + j
                    next_nodes.append((child, k))
                    most_left = min(most_left, k)
                    most_right = max(most_right, k)
            width = max(width, most_right - most_left + 1)
            nodes = next_nodes
        return width
