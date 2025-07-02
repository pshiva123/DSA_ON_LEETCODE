# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li=[]
        for item in lists:
            while item:
                heapq.heappush(li,item.val)
                item=item.next
        if len(li)==0:
            return None
        x=heapq.heappop(li)
        head=ListNode(x)
        temp=head
        while li:
            t=heapq.heappop(li)
            temp.next=ListNode(t)
            temp=temp.next
        return head

        
