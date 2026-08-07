# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = fastPointer = head

        while slowPointer and fastPointer:
            slowPointer = slowPointer.next if slowPointer.next else None
            fastPointer = fastPointer.next.next if fastPointer.next and fastPointer.next.next else None

            if slowPointer and fastPointer and slowPointer == fastPointer:
                return True


        return False
        