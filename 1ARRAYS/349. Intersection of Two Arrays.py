# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 
class sol(object):

    def intersection(self,nums1,nums2):
        result = []
        for i in nums1:
            if (i in nums2) and (i not in result):
                result.append(i)
        return result

Sol=sol()

nums1=[4,5,5,6,7]
nums2=[5 ,6,7,1,2,3,8,9]

print(Sol.intersection(nums1,nums2))