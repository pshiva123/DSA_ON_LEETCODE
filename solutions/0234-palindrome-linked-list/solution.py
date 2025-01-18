# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        first=head
        second=reversell(slow.next)
        while second:
            if first.val==second.val:
                first=first.next
                second=second.next
            else:
                return False
        return True
def reversell(temp):
    if temp is None or temp.next is None:
        return temp
    newhead=reversell(temp.next)
    front=temp.next
    front.next=temp
    temp.next = None
    return newhead


        
