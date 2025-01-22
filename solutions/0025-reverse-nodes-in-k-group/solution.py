# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevNode=None
        temp=head
        while temp:
            kthnode=findkthnode(temp,k)
            if kthnode==None:
                if prevNode:
                    prevNode.next=temp
                break
            nextnode=kthnode.next
            kthnode.next=None
            reverselist(temp)
            if temp==head:
                head=kthnode
            else:
                prevNode.next=kthnode     
            prevNode=temp
            temp=nextnode
        return head
def findkthnode(temp,k):
    k-=1
    while k and temp:
        temp=temp.next
        k-=1
    return temp
def reverselist(head):
    if head is None or head.next is None:
        return head
    newhead=reverselist(head.next)
    front=head.next
    front.next=head
    head.next=None
    return newhead

            
        
