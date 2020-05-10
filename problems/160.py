class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        nodeA = headA
        nodeB = headB
        while id(nodeA) != id(nodeB):
            nodeA = nodeA.next
            nodeB = nodeB.next
            if nodeA is None and nodeB is None:
                return None
            elif nodeA is None:
                nodeA = headB
            elif nodeB is None:
                nodeB = headA
        return nodeA
