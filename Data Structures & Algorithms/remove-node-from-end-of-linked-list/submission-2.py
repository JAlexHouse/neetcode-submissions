# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leftPointer = dummy = ListNode(0, head)
        rightPointer = head

        for i in range(n):
            rightPointer = rightPointer.next

        while rightPointer:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

        leftPointer.next = leftPointer.next.next

        return dummy.next