# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the merged list
        dummy = ListNode(-1)
        # Pointer to the current node of the merged list
        current = dummy
        
        # Traverse both lists simultaneously
        while list1 is not None and list2 is not None:
            # Compare the values of the nodes and append the smaller one to the merged list
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the pointer in the merged list
            current = current.next
        
        # Append the remaining nodes of list1 or list2
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        
        # Return the merged list starting from the next node of the dummy node
        return dummy.next
