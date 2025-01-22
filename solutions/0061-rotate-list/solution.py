# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k==0:
            return head
        l=findlen(head)
        #print(l)
        k=k%l
        k=l-k
        temp=head
        k-=1
        #print(k)
        while temp.next and k:
            temp=temp.next
            k-=1
        newhead=temp.next
        temp.next=None
        temp2=newhead
        #print(temp.val)
        while temp2 and temp2.next:
            temp2=temp2.next
        if temp2:
            temp2.next=head
        else:
            return head
        return newhead
def findlen(temp):
    c=0
    while temp:
        temp=temp.next
        c+=1
    return c

        
