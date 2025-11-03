# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution(object):
    def valpal(self,s):
        new_s= "".join(c.lower() for c in s if c.isalnum())
        lst=list(new_s)[::-1]
        rev="".join(lst)

        return new_s==rev

        # left=0
        # right=len(new_s)-1

        # while left < right:
        #     if new_s[left]!=new_s[right]:
        #         return False
        #     left+=1
        #     right -=1
        # return True


s="MADAMM"
sol=Solution()
print("{s}",sol.valpal(s))

