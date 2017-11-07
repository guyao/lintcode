# http://lintcode.com/en/problem/remove-duplicates-from-sorted-list

# Definition of ListNode


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of linked list
    """

    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(None)
        dummy.next = head
        head = dummy
        while head is not None:
            while head.next is not None and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return dummy.next


h = ListNode(1)
h.next = ListNode(1)
h.next.next = ListNode(1)
h.next.next.next = ListNode(3)

r = Solution().deleteDuplicates(h)
