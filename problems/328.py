from itertools import count


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        tmp_even_head = ListNode()
        tmp_odd_head = ListNode()
        node = head
        even_node, odd_node = tmp_even_head, tmp_odd_head
        cnt = count(1)
        while node is not None:
            if next(cnt) % 2:    # odd
                odd_node.next = node
                odd_node = node
            else:   # even
                even_node.next = node
                even_node = node
            node = node.next
        odd_node.next = tmp_even_head.next
        even_node.next = None
        return tmp_odd_head.next
