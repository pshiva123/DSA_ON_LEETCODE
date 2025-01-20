# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle=findmiddle(head)
        right_head=middle.next
        middle.next=None

        leftnode=self.sortList(head)
        rightnode=self.sortList(right_head)

        return mergesortedlists(leftnode,rightnode)
def findmiddle(temp):
    if temp is None or temp.next is None:
        return temp
    slow=temp
    fast=temp
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
    return slow
def mergesortedlists(left,right):
    dummy=ListNode(0)
    temp=dummy
    while left and right:
        if left.val<right.val:
            temp.next=left
            left=left.next
        else:
            temp.next=right
            right=right.next
        temp=temp.next
    if right:
        temp.next=right
    if left:
        temp.next=left
    return dummy.next



