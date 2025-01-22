# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def findmiddle(temp):
            slow=temp
            fast=temp
            while fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        def reverselist(temp):
            if temp is None or temp.next is None:
                return temp
            newhead=reverselist(temp.next)
            front=temp.next
            front.next=temp
            temp.next=None
            return newhead
        middle=findmiddle(head)
        first=head
        second=middle.next
        second=reverselist(second)
        middle.next=None
        s=0
        while second:
            s=max(first.val+second.val,s)
            second=second.next
            first=first.next
        return s

        
