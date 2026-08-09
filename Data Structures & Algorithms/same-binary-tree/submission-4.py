# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pstack = [p]
        qstack = [q]

        while pstack and qstack:
            pNode = pstack.pop()
            qNode = qstack.pop()

            if not pNode and not qNode:
                continue
            elif not pNode or not qNode or pNode.val != qNode.val:
                return False

            pstack.append(pNode.left)
            qstack.append(qNode.left)
            pstack.append(pNode.right)
            qstack.append(qNode.right)

        return True