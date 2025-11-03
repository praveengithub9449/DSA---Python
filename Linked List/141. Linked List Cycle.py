""" 141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # cycle detected
                return True

        return False


# ----------------------
# Helper function to create a linked list with optional cycle
# ----------------------
def create_linked_list(lst, pos=-1):
    """
    lst: list of values
    pos: index where the tail connects (-1 means no cycle)
    """
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head
    nodes = [head]  # keep references to nodes

    for val in lst[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        nodes.append(new_node)

    # Create cycle if pos is valid
    if pos != -1:
        current.next = nodes[pos]

    return head


# ----------------------
# Example Tests
# ----------------------
sol = Solution()

# Example 1: [3,2,0,-4], pos = 1 → cycle exists
head1 = create_linked_list([3,2,0,-4], pos=1)
print(sol.hasCycle(head1))  # True

# Example 2: [1,2], pos = 0 → cycle exists
head2 = create_linked_list([1,2], pos=0)
print(sol.hasCycle(head2))  # True

# Example 3: [1], pos = -1 → no cycle
head3 = create_linked_list([1], pos=-1)
print(sol.hasCycle(head3))  # False
