# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1=headA
        temp2=headB
        while temp1!=temp2:
            if temp1 is None:
                temp1=headB
            elif temp2 is None:
                temp2=headA
            if temp1==temp2:
                break
            temp1=temp1.next
            temp2=temp2.next
        return temp1


        
