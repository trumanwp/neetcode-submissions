# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        # Deque used, initialise with root
        # For each node, popleft, add children to queue, save popleft as our right value
        # Once all nodes in the level have been iterated through, we add right value to res

        res = []
        queue = deque([root])

        while queue:
            rightVal = None
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr:
                    rightVal = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if rightVal:
                res.append(rightVal.val)
        
        return res
