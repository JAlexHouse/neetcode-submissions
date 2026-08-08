# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        rightPointer = head

        for i in range(n-1):
            rightPointer = rightPointer.next

        leftPointer = dummy
        while rightPointer and rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next
            print(leftPointer.val, rightPointer.val if rightPointer else None)

        leftPointer.next = leftPointer.next.next if leftPointer and leftPointer.next else None

        return dummy.next