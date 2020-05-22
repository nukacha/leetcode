from collections import deque


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def __init__(self):
        self.stack = deque()

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        if head.child:
            if head.next:
                self.stack.append(head.next)
            head.next, head.child = head.child, None
        if head.next is None and self.stack:
            head.next = self.stack.pop()
        if head.next:
            head.next.prev = head
            self.flatten(head.next)
        return head
