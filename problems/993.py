class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        node_list = [root]
        xy_flag = False
        xy = (x, y)
        while node_list:
            child_node_list = list()
            for node in node_list:
                left, right = node.left, node.right
                left_v, right_v = 0, 0
                if left:
                    left_v = left.val
                    child_node_list.append(left)
                if right:
                    right_v = right.val
                    child_node_list.append(right)
                if left_v in xy and right_v in xy:
                    return False
                elif left_v in xy or right_v in xy:
                    if xy_flag:
                        return True
                    xy_flag = True
            if xy_flag:
                return False
            node_list = child_node_list
        return False
