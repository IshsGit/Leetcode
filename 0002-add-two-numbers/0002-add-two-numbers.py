# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize result linked list and current node pointer
        result_head = ListNode(0)
        current = result_head
        carry = 0
        
        # Traverse both input linked lists
        while l1 or l2 or carry:
            # Get values from l1 and l2 (or default to 0 if None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            sum_val = val1 + val2 + carry
            carry = sum_val // 10  # Get the new carry
            sum_val = sum_val % 10  # Get the new node value
            
            # Create a new node with the sum value
            current.next = ListNode(sum_val)
            current = current.next
            
            # Move to the next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the head of the result linked list (skip the initial dummy node)
        return result_head.next
