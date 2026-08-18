# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, tes: Optional[TreeNode]) -> bool:
        if not tes:
            return True
        def isValid(node, ceil, floor):
            if not node:
                return True
            isLeftValid = not node.left or isValid(node.left, node.val, floor)
            isRightValid = not node.right or isValid(node.right, ceil, node.val)

            return floor < node.val < ceil and isLeftValid and isRightValid
        
        return isValid(tes, float("inf"), float("-inf"))