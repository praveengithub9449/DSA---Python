"""25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def reverseKGroup(self, head, k):
        count=0
        temp=head

        while temp:
            count +=1
            temp=temp.next 

        dummy =ListNode(0)
        dummy.next=head
        prev=dummy

        while count >= k:
            cur=prev.next
            next_node=cur.next

            for _ in range (1,k):
                cur.next=next_node.next
                next_node.next=prev.next
                prev.next=next_node
                next_node=cur.next
            
            prev=cur
            count -= k
        return dummy.next


            
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
deleted=sol.reverseKGroup(head,2)
printList(deleted)
