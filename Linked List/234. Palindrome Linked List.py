"""
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false

"""
class ListNode(object ):
    def __init__ (self,val=0,next =None):
         self.val=val
         self.next=next
        
class Solution(object):
    def isPalindrome(self, head):
        arr=[]
        temp=head

        while temp:
            arr.append(temp.val)
            temp=temp.next
        return arr==arr[::-1]
    
def CreateList(list):
    if not list:
        return None
    head=ListNode(list[0])
    current=head

    for val in list[1:]:
        current.next =ListNode(val)
        current=current.next
    return head
def printList(head):
    values=[]

    values.append(str(head.val))
    print("->".join(values))

head=CreateList([1,2,2,1]  )
sol=Solution()
printList(head)                 # Prints: 1->2->2->1
print(sol.isPalindrome(head)) 