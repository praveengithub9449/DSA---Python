"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        count =0
        temp =head 

        while temp:
            count +=1
            temp=temp.next
        mid =count //2

        temp=head
        for _ in range (mid):
            temp=temp.next
        return temp
    
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    temp = head
    for val in lst[1:]:
        temp.next = ListNode(val)
        temp = temp.next
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
ans= sol.middleNode(head)
print_linked_list(ans)