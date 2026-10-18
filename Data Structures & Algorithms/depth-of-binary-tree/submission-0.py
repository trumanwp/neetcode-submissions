# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        # Set a depth val to 0
        # Recursively traverse the tree until null nodes are hit
        # if node isnt null, give it a value of +1, compare both nodes in subtree, take max value
        # keep going til at root, return the value

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
