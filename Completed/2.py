# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        result = ListNode(0, None)
        carry = 0
        trav1 = l1
        trav2 = l2

        result_trav = result

    #    add each digit and carry the remainder 
        while trav1 != None and trav2 != None:
            sum_val = (trav1.val + trav2.val) + carry
            carry = sum_val // 10

            result_trav.next = ListNode(sum_val - (carry * 10), None)

            # move forward
            result_trav = result_trav.next
            trav1 = trav1.next
            trav2 = trav2.next
        
        # if l1 longer
        while trav1 != None:
            val = 0
            if carry != 0:
                sum_val = (trav1.val) + carry
                carry = sum_val // 10
                val = sum_val - (carry * 10)
            else:
                val = trav1.val

            result_trav.next = ListNode(val, None)

            result_trav = result_trav.next
            trav1 = trav1.next

        # if l2 longer
        while trav2 != None:
            val = 0
            if carry != 0:
                sum_val = (trav2.val) + carry
                carry = sum_val // 10
                val = sum_val - (carry * 10)
            else:
                val = trav2.val

            result_trav.next = ListNode(val, None)

            result_trav = result_trav.next
            trav2 = trav2.next

        # in case even length lists that create a new digit
        if carry != 0:
            result_trav.next = ListNode(carry, None)
            result_trav = result_trav.next

        
        return result.next