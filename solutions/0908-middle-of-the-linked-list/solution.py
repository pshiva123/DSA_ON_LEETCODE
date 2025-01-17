# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp1=head
        temp2=head
        while(temp2.next.next):
            temp1=temp1.next
            temp2=temp2.next.next
            if temp2 is None or temp2.next is None:
                break
        if temp2.next:
            return temp1.next
        return temp1
        
