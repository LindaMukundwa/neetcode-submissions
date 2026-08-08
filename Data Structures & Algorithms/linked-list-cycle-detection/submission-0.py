# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # try using a hashset to keep track of visited
        # iterate through list, add to set, check if in set

         # Using a set to store visited nodes (not values)
        visited = set()
        
        while head:
            # Check if this node has been visited before
            if head in visited:
                return True
            # Add current node to visited set
            visited.add(head)
            # Move to next node
            head = head.next
            
        # If we reach the end, there's no cycle
        return False
            