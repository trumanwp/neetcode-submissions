# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        nodes = []

        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
            
        nodes.sort()
        
        # convert to linked list

        res = ListNode(0)
        curr = res

        # curr [0,1,2,3,4,5]
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        
        return res.next

            




