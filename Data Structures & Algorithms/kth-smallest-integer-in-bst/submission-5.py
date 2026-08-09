# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        bst = [root]

        while bst:
            n = bst.pop()
            if n:
                heapq.heappush(heap, n.val)
                if n.left:
                    bst.append(n.left)
                if n.right:
                    bst.append(n.right)
        for i in range(k-1):
            heapq.heappop(heap)
        return heap[0]
            