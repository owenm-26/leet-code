# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
       
        fast, slow = head, head
        prev = None

        # reverse the first half and get the start of front and back (prev and slow)
        while fast and fast.next:
            fast = fast.next.next
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
            
        # find the best twin sum
        best = 0
        
        while prev: #and slow
            best = max(best, prev.val + slow.val)
            slow = slow.next
            prev = prev.next
        
        return best
        


        
    

        