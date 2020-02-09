"""
Definition of ListNode
"""


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):
    """
    @param: head: ListNode head is the head of the linked list 
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """

    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(None)
        dummy.next = head
        head = dummy
        prev = None
        for i in range(m):
            if head is None:
                return None
            prev = head
            head = head.next
        prenode = prev
        mnode = head
        prev = None
        for i in range(n - m + 1):
            head.next, prev, head = prev, head, head.next
        prenode.next = prev
        mnode.next = head
        return dummy.next


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
r = Solution().reverseBetween(h, 2, 4)