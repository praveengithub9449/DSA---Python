"""83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

class ListNode(object):
    def __init__ (self,val=0,next=None):
        self.val=val
        self.next=None

class Solution(object):
    def deleteDuplicates(self, head):
       
        temp=head

        while temp and temp.next:

            if temp.val == temp.next.val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return head
    
def Create_List(list):
    if not list:
        return None

    head=ListNode(list[0])
    current=head
    for val in list[1:]:
        current.next=ListNode(val)
        current=current.next

    return head

def printList(head):
    values=[]
    while head:
        values.append(str(head.val))
        head=head.next
    print("->".join(values))

head=Create_List( [1,1,3,4,4,5,5])
sol=Solution()
deleted=sol.deleteDuplicates(head)
printList(deleted)
