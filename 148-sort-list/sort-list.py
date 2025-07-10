# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        l = []
        while(temp!=None):
            l.append(temp.val)
            temp=temp.next
        l.sort()
        temp=head
        for val in l:
            temp.val=val
            temp=temp.next
        return head
        