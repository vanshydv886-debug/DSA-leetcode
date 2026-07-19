# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        t1 = l1
        t2 = l2

        dummy = ListNode(-1)
        curr = dummy

        carry = 0

        while t1 is not None or t2 is not None:

            total = carry

            if t1 is not None:
                total += t1.val

            if t2 is not None:
                total += t2.val

            newNode = ListNode(total % 10)

            carry = total // 10

            curr.next = newNode
            curr = curr.next

            if t1 is not None:
                t1 = t1.next

            if t2 is not None:
                t2 = t2.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next
        