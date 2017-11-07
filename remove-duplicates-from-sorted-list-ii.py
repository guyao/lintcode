# http://lintcode.com/en/problem/remove-duplicates-from-sorted-list-ii


# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of the linked list
    """

    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(None)
        dummy.next = head
        head = dummy
        while head.next is not None and head.next.next is not None:
            if head.next.val == head.next.next.val:
                v = head.next.val
                while head.next is not None and head.next.val == v:
                    head.next = head.next.next
            else:
                head = head.next
        return dummy.next


h = ListNode(10)
h.next = ListNode(11)
h.next.next = ListNode(11)
h.next.next.next = ListNode(12)
h.next.next.next.next = ListNode(26)
r = Solution().deleteDuplicates(h)
