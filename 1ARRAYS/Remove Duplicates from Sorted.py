"""
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""

def Dup(nums):
    n=len(nums)
    k=1

    for i in range(1,n):
        if (nums[i]!=nums[i-1]):
            nums[k]=nums[i]
            k+=1
    return k,nums[:k]




nums=[1,1,2]
print("length of k:",Dup(nums) )