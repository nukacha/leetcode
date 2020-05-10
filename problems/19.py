class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        target_prev = ListNode(next=head)
        tail = head
        for _ in range(n):
            tail = tail.next
        while tail is not None:
            target_prev = target_prev.next
            tail = tail.next
        if id(target_prev.next) == id(head):
            return head.next
        target_prev.next = target_prev.next.next
        return head
