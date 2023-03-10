# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        dummy = head
        currNode = head
        nextNode = currNode.next
        prevNode = None
        
        while nextNode != None:
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            nextNode = currNode.next
        
        currNode.next = prevNode
        return currNode