class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        node = head
        length = 1
        while node.next:
            length += 1
            node = node.next
        else:
            node.next = head
        k = k % length
        node = head
        for _ in range(length - k - 1):
            node = node.next
        r_head, node.next = node.next, None
        return r_head
