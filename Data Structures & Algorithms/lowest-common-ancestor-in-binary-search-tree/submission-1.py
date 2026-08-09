# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        toSearch = [root]

        # make p always the smaller one
        if p.val > q.val:
            p, q = q, p

        while toSearch:
            node = toSearch.pop()
            if node.left and node.val > p.val and node.val > q.val:
                toSearch.append(node.left)
            elif node.right and node.val < p.val and node.val < q.val:
                toSearch.append(node.right)
            elif node.val >= p.val and node.val <= q.val:
                return node