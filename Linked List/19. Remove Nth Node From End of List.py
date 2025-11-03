
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
"""

class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def removeNthFromEnd(self, head, n):
       
        length =0
        position=0
        
        temp=head

        while temp:
            length +=1
            temp=temp.next
        
        position=length - n

        if position ==0:
            return head.next
        
        temp=head
        for _ in range (position-1):
            temp=temp.next

        temp.next=temp.next.next
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

head=Create_List( [1,2,3,4,5])
sol=Solution()
n=int(input("Enter the num"))
printList(sol.removeNthFromEnd( head, n))
    