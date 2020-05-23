class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node_dict = {id(None): None}
        node = head
        while node:
            node_dict[id(node)] = Node(
                                    node.val,
                                    node.next,
                                    node.random)
            node = node.next
        node = head
        while node:
            node_copy = node_dict[id(node)]
            node_copy.random = node_dict[id(node_copy.random)]
            node_copy.next = node_dict[id(node_copy.next)]
            node = node.next
        return node_dict[id(head)]
