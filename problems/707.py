class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def get(self, index: int) -> int:
        node = self.getNode(index)
        if node is None:
            return -1
        else:
            return node.val
    
    def getNode(self, index: int) -> ListNode:
        if not (-1 < index < self.length):
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        node = ListNode(val)
        if index == 0:
            node.next, self.head = self.head, node
            self.length += 1
            return
        prev_node = self.getNode(index - 1)
        if prev_node is None:
            return
        if prev_node.next is not None:
            node.next = prev_node.next
        prev_node.next = node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        node = self.getNode(index - 1)
        if node is None or node.next is None:
            return
        node.next = node.next.next
        self.length -= 1
