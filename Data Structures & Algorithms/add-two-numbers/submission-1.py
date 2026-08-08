# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum = dummy = ListNode()
        while l1 or l2:
            sumTemp = 0
            if l1 and not l2:
                sumTemp = l1.val + carry
                l1 = l1.next
            elif not l1 and l2:
                sumTemp = l2.val + carry
                l2 = l2.next
            else:
                sumTemp = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            dummy.next = ListNode(sumTemp % 10)
            carry = sumTemp // 10
            dummy = dummy.next

        if carry:
            dummy.next = ListNode(1)

        return sum.next