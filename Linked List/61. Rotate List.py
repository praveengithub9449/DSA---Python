"""Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 """
class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def rotateRight(self, head, k):

        if not head or not head.next or k==0:
            return head

        temp=head
        length=1

        while temp.next:
            temp=temp.next
            length +=1
        
        k=k%length
        if k==0:
            return head

        new_last=head
        for _ in range(length-k-1):
            new_last=new_last.next
                
            
        new_head=new_last.next
        new_last.next=None
        temp.next=head


        return new_head
    
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
deleted=sol.rotateRight(head,2)
printList(deleted)
