"""Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []  """

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative reverse linked list
class Solution(object):
    def reverseList(self, head):
        prev = None
        temp = head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        return prev

# Helper function to create linked list from Python list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        
        current = current.next
        
    return head

# Helper function to print linked list
def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" → ".join(vals))

# Test
sol = Solution()
head = create_linked_list([1, 2,3,4,5,6])
reversed_head = sol.reverseList(head)
print_linked_list(reversed_head)

