# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

class Solution (object ):
    def Unique(self, s):
        c={}
        for char in s:
            c[char]=c.get(char,0)+1
        
        for i ,char in enumerate (s):
            if c[char] == 1:

                return i
        return -1

Sol=Solution()

s="loveleetcode"

print(Sol.Unique(s))
