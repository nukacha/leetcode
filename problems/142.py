class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_set = set()
        node = head
        while node is not None:
            if node in node_set:
                return node
            node_set.add(node)
            node = node.next
        return None
