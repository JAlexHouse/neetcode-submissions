from _heapq import heapify
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        dummy = head = ListNode()
        
        while heap:
            pop = heapq.heappop(heap)
            dummy.next = ListNode(pop)
            dummy = dummy.next

        
        return head.next