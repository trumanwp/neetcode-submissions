# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ 
        2 pointers solution
        - create dummy ListNode(0, head)
        - create left and right pointers, from dummy and head
        - for each value of n, move right pointer and decrease n (n = 2, right pointer moves 2 places, until n = 0)
        - then, while right: (while rights isnt falsy, i.e, isnt None)
            - iterate both left and right pointers at the same time
            - when the loop breaks, right will be on final node, and left will be on [-n] node,
              the one before the one we need to remove
            - set the next pointer of left, to nextnext
        
        ----------

        The idea behind this solution is that because the n node we need to remove is equal to len(nodes) - 1, we can use 2
        pointers to find out 
        - the length of the list, with right pointer
        - the node before n, with the left pointer
        - we initially move right pointer forward n spaces, and iterate both pointers until right = None, at which point left will be 
          right before n, and we can change the next pointer
        """
        
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            n -= 1
            right = right.next
            
        
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next

        return dummy.next
        



    
