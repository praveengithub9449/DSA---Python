
"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


class Solution(object):
     
    def findKthPositive(self, arr, k):
            missing=[]
            nums=1
            i=0         
            while len(missing)<k:
                if i< len(arr) and arr[i]==nums:
                    i +=1
                else:
                    missing.append(nums)
                nums +=1
            return missing[-1]

sol=Solution()
arr=[2,3,4,7,11]
k = 5

print(sol.findKthPositive(arr, k))

"""
class Solution(object):
    def findKthPositive(self, arr, k):
        left= 0
        right = len(arr)-1
        
        while left <= right :
            mid = (left+right ) // 2
            miss_count = arr[mid]-(mid +1)
        
            if miss_count< k:
                left=mid+1
            
            else:
                right=right-1
        return left+k