# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        q = [(root, float("-inf"))]

        res = 0
        while q:
            node, reqMin = q.pop()

            if node.val >= reqMin:
                res += 1
            
            if node.left:
                q.append((node.left, max(node.val, reqMin)))
            
            if node.right:
                q.append((node.right, max(node.val, reqMin)))
        
        return res
