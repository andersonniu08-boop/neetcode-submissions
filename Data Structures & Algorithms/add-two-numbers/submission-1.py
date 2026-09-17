# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 and l2:
            val = carry + l1.val + l2.val
            tmp = ListNode(val)
            if val >= 10:
                carry = 1
                tmp.val -= 10
            else:
                carry = 0
            curr.next = tmp
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val = carry + l1.val
            tmp = ListNode(val)
            if val >= 10:
                carry = 1
                tmp.val -= 10
            else:
                carry = 0
            curr.next = tmp
            curr = curr.next
            l1 = l1.next      
        while l2:
            val = carry + l2.val
            tmp = ListNode(val)
            if val >= 10:
                carry = 1
                tmp.val -= 10
            else:
                carry = 0
            curr.next = tmp
            curr = curr.next
            l2 = l2.next   

        if carry == 1:
            tmp = ListNode(1)
            curr.next = tmp


        return dummy.next       
        