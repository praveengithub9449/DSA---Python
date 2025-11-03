# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:
# Input: nums = [2,7,11,11], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution(object):
    def sum(self,nums,target):

        num_ind={}
        
        print(list(enumerate(nums)))
        for i,num in enumerate(nums):
            
            diff=target-num

            if diff in num_ind:
                return [num_ind[diff],i]
                
            
            num_ind[num]=i 
            print(num_ind)
        

sol=Solution()

nums=[2,7,11,11]
target = 22

print(sol.sum(nums,target))
