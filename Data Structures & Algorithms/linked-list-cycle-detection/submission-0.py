# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        currentNode, temp= head, head
        while currentNode and currentNode.next:
            temp = temp.next
            currentNode = currentNode.next.next
            if currentNode == temp:
                return True

        return False
            



