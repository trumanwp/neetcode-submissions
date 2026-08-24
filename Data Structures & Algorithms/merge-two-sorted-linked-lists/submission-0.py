# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create an empty head to be the start of the new list
        #create a current node, which will track pos and increase
        dummy = ListNode() #this node stays here
        current = dummy

        #loop through both lists
        #if list1.val < list2.val, 
            #list1 is the next node
            #list1 = list1.next, making list1 move up to its next node

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # we set current.next to its next counter,
            # after the conditional we need to move current to it
            # as current is our pos pointer
            current = current.next

        # once a list is empty, it adds the rest of the remaining list
        current.next = list1 if list1 else list2

        # dummy is the empty head we created
        # we need to return the actual head, i.e, dummy.next
        return dummy.next
            
        
