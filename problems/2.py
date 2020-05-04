class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_node_to_int(l: ListNode) -> int:
    r = 0
    order = 1
    while True:
        r += l.val * order
        if l.next is None:
            break
        order *= 10
        l = l.next
    return r


def int_to_list_node(n: int) -> ListNode:
    n_str = str(n)[::-1]
    r = ListNode(val=int(n_str[0]))
    l = r
    for val_str in n_str[1:]:
        l.next = ListNode(int(val_str))
        l = l.next
    return r


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = list_node_to_int(l1)
        n2 = list_node_to_int(l2)
        return int_to_list_node(n1 + n2)
