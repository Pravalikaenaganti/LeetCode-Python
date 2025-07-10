class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def findMiddle(head):
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = None  
    return slow

def merge(left, right):
    dummy = ListNode()
    tail = dummy
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    tail.next = left or right
    return dummy.next

class Solution:
    def sortList(self, head): 
        if not head or not head.next:
            return head

        mid = findMiddle(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
