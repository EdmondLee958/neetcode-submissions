# Definition for singly-linked list.
# class ListNode:
#from types import new_class
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1, l2 = list1, list2

        res = ListNode (0)
        curr = res

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
            elif l2.val < l1.val:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = ListNode(l1.val)
                curr = curr.next
                curr.next = ListNode(l2.val)
                curr = curr.next
                l1 = l1.next
                l2 = l2.next

        curr.next = l1 if l1 else l2
        return res.next

