# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


        if head.next == None:
            head.val = ''
            return head
        
        # create dummy node to point at beginning 
        slow, fast = ListNode(), head
        slow.next = head
        
        # move the fast pointer twice as fast
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # skip the middle once loop exited
        if slow.next: 
            slow.next = slow.next.next
        return head
        
        
        # length = 1
        # trav = head
        # while trav.next:
        #     length +=1
        #     trav = trav.next
        
        # if length == 1:
        #     head.val = ''
        #     head.next = None
        #     return head
        # if length == 2:
        #     head.next = None
        #     return head

        # mid = length //2 
        # trav = head
        # trailer = None
        # for i in range(mid+1):
        #     if i == mid:
        #         trailer.next = trav.next
        #         break
        #     else:
        #         trailer = trav
        #         trav = trav.next
        # return head