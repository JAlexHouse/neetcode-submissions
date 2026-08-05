# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxDepth = 0
        stack = [(1, root)]

        while stack:
            nodeWithDepth = stack.pop()
            maxDepth = max(nodeWithDepth[0], maxDepth)
            if nodeWithDepth[1] and nodeWithDepth[1].left:
                stack.append((nodeWithDepth[0] + 1, nodeWithDepth[1].left))
            if nodeWithDepth[1] and nodeWithDepth[1].right:
                stack.append((nodeWithDepth[0] + 1, nodeWithDepth[1].right))
        
        return maxDepth

