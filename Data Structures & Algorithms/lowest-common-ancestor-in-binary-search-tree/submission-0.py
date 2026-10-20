# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # start at root
        # if p and q are both less than root, call function again from root.left
        # if p and q are both greater than root, call again from root.right
        # otherwise, if root is between values of p and q, return root, its the lca

        if not root:
            return None
        
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root