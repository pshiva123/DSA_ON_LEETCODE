# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if head.next:
            head.val,head.next.val=head.next.val,head.val
        temp=head.next.next
        while temp and temp.next:
            temp.val,temp.next.val=temp.next.val,temp.val
            temp=temp.next.next
        return head
            


        
