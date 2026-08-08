# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        # use iterative approach by reversing direction of next pointer
        # at each node
        
        while current:
            # Save the next node before we break the link
            temp = current.next
            # Reverse the pointer to point backwards
            current.next = previous
            # Move previous forward to current position
            previous = current
            # Move current forward to the saved next node
            current = temp
        return previous 