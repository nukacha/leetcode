class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node1 = head
        node2 = head
        while node2 is not None and node2.next is not None:
            node1 = node1.next
            node2 = node2.next.next
        node2 = head
        node1 = self.reverseList(node1)
        while node1 is not None:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True
            
    def reverseList(self, head: ListNode) -> ListNode:
        # FIXME: Due to recursion, not O(1) space
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
