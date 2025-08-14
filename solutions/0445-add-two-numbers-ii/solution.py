# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseli(li):
            if li is None or li.next is None:
                return li
            new_head=reverseli(li.next)
            li.next.next=li
            li.next=None
            
            return new_head
        
        reversedl1=reverseli(l1)
        reversedl2=reverseli(l2)
        carry=0
        dummy=ListNode(0)
        headd=dummy
        while reversedl1 and reversedl2:
            s=reversedl1.val+reversedl2.val+carry
            if s>=10:
                carry=1
                s=s-10
            else:
                carry=0
            dummy.next=ListNode(s)
            dummy=dummy.next
            reversedl1=reversedl1.next
            reversedl2=reversedl2.next
        while reversedl1:
            s=reversedl1.val+carry
            if s>=10:
                carry=1
                s=s-10
            else:
                carry=0
            dummy.next=ListNode(s)
            dummy=dummy.next
            reversedl1=reversedl1.next
        while reversedl2:
            s=reversedl2.val+carry
            if s>=10:
                carry=1
                s=s-10
            else:
                carry=0
            dummy.next=ListNode(s)
            dummy=dummy.next
            reversedl2=reversedl2.next
        if carry==1:
            dummy.next=ListNode(carry)
        headd=headd.next
        return reverseli(headd)
        
                
        
