class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp_head = ListNode(next=head)
        node = tmp_head
        while node is not None and node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return tmp_head.next
