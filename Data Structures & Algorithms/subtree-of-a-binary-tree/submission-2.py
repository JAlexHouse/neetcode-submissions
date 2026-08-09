# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find root of subroot inside of root
        bfs = [root]
        pCandidates = []
        while bfs:
            p = bfs.pop()

            if p and subRoot and p.val == subRoot.val:
                pCandidates.append(p) # found subroot root inside of main tree
            
            if p and p.left:
                bfs.append(p.left)
            if p and p.right:
                bfs.append(p.right)
        
        if not pCandidates:
            return False
            
        return any(self.evalCandidates(p, subRoot) for p in pCandidates)

    def evalCandidates(self, p, subRoot) -> bool:
        pstack = [p]
        qstack = [subRoot]

        # iterate through both trees to see if identical
        while pstack and qstack:
            pNode = pstack.pop()
            qNode = qstack.pop()

            if not pNode and not qNode:
                continue
            elif not pNode or not qNode or pNode.val != qNode.val:
                return False
            else:
                pstack.append(pNode.left)
                pstack.append(pNode.right)
                qstack.append(qNode.left)
                qstack.append(qNode.right)
        return True
        