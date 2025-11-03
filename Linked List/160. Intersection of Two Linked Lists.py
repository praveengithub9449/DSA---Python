""""Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.
Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null."""


class ListNode(object):
    def __init__ (self,val=0,next=None):
        self.val=val
        self.next=None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def findLength(LinkedList):
            length=0
            while LinkedList:
                length +=1
                LinkedList=LinkedList.next
            return length
        
        lenA=findLength(headA)
        lenB= findLength(headB)

        while lenA>lenB:
            headA=headA.next
            lenA -= 1

        while lenB>lenA:
            headB=headB.next
            lenB -= 1

        while headA!= headB:

            headA=headA.next
            headB=headB.next
        return headA


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

headA=Create_List( [4,1,8,4,5])
headB=Create_List( [5,6,1,8,4,5])

sol=Solution()
deleted=sol.getIntersectionNode(headA,headB)
printList(deleted)
        