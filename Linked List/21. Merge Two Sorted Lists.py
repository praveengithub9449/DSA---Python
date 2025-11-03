"""
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remainder
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next


# ------------------------------
# Helpers

def create_linked_list(lst):
    """Convert Python list -> Linked List"""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    """Print Linked List as values joined by ->"""
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print("->".join(values) if values else "[]")


# ------------------------------
# Test Examples

sol = Solution()

# Example 1
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged = sol.mergeTwoLists(list1, list2)
print_linked_list(merged)   # Expected: 1->1->2->3->4->4

# Example 2
list1 = create_linked_list([])
list2 = create_linked_list([])
merged = sol.mergeTwoLists(list1, list2)
print_linked_list(merged)   # Expected: []

# Example 3
list1 = create_linked_list([])
list2 = create_linked_list([0])
merged = sol.mergeTwoLists(list1, list2)
print_linked_list(merged)   # Expected: 0
