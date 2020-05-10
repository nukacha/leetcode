class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        node1 = head    # slow pointer
        node2 = head.next   # fast pointer
        while node1 != node2:
            if node2 is None or node2.next is None:
                return False
            node1 = node1.next
            node2 = node2.next.next
        return True
