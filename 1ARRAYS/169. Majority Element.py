# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Sln(object):
    def MjrEle(self,nums):
        for x in set(nums):
            print(set(nums))
            if nums.count(x) > len(nums) //2 :                
                return x

nums=[2,2,1,1,1,2,2]


sol=Sln()


print("mejority element is repeted " ,sol.MjrEle(nums ))

    