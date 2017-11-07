"""
Definition of ListNode
"""


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        fp = head.next
        sp = head
        while fp != sp:
            if fp is None or fp.next is None:
                return False
            fp = fp.next.next
            sp = sp.next
        return True
