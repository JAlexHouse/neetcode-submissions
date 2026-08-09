# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get a pointer to the middle of the list (two pointers)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the right half of the list
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        dummy = head
        revTemp = prev
        # coalesce the first half and the second half, alternating between the two
        while revTemp.next:
            temp = dummy.next
            dummy.next = revTemp
            revTemp = revTemp.next
            dummy = dummy.next
            dummy.next = temp
            dummy = dummy.next
            