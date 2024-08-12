# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # explanation: keep track of the previous, current, and next nodes
        if not head or head.next == None:
            return head
        
        trav = head.next
        prev = head
        nextNode = None
       
        while trav and trav.next:
            nextNode = trav.next 
            trav.next = prev
            prev = trav
            trav = nextNode    

        head.next = None     
        trav.next = prev   
        return trav