# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def divide(lists: List[Optional[ListNode]], l, r) -> Optional[ListNode]:
            if l > r:
                return None
            if l == r:
                return lists[l]
            mid = (l + r) // 2
            leftHalf = divide(lists, l, mid)
            rightHalf = divide(lists, mid + 1, r)
            return conquer(leftHalf, rightHalf)

        def conquer(listA, listB):
            dummy = res = ListNode()

            while listA and listB:
                if listA.val < listB.val:
                    dummy.next = listA
                    listA = listA.next
                    dummy = dummy.next
                else:
                    dummy.next = listB
                    listB = listB.next
                    dummy = dummy.next
            
            dummy.next = listA or listB
            return res.next
        return divide(lists, 0, len(lists) - 1)