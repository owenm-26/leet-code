# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = None
        # initialize head
        if list1 and list2 and list1.val <= list2.val:
            head = list1
            list1 = list1.next
        elif list1 and list2 and list1.val > list2.val:
            head = list2
            list2 = list2.next
        # one of the lists is empty
        else:
            if list1 is None:
                return list2
            else:
                return list1

        builder = head
        while list1 != None and list2!=None:
            if list1.val <= list2.val:
                builder.next = list1
                list1 = list1.next
            else:
                builder.next = list2
                list2 = list2.next
            builder = builder.next

        builder.next = list1 if list1 else list2

        return head
        