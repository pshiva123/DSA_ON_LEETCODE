"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def step1(self,head):
        while(head):
            temp=head.next
            head.next=Node(head.val)
            head.next.next=temp
            head=temp
    def step2(self,head):
        while(head):
            newhead=head.next
            if head.random:
                newhead.random=head.random.next
            head=head.next.next
    def step3(self,head):
        ans=head.next
        temp=ans
        while(head):
            head.next=head.next.next
            if temp.next:
                temp.next=temp.next.next
            head=head.next
            temp=temp.next
        return ans

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        self.step1(head)
        self.step2(head)
        return self.step3(head)

        
        
        
