# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to keep node
        dummy = node = ListNode()
        # while the lists exist
        #Uses a node pointer to build the new list, returns dummy.next 
        # to get the actual merged list, only compares while both lists have nodes
        # Always picks the smaller value between list1.val and list2.val
        # Moves the chosen list pointer forward
        while list2 and list1:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        # attaches whatever non-empty list remains, works because None is falsy in Python
        node.next = list1 or list2

        return dummy.next
