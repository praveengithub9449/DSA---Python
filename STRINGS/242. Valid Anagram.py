# 242. Valid Anagram

        
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

 class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        cc={}
        for char in s:
            cc[char]=cc.get(char,0)+1
        
        for char in t:
            if char not in cc or cc[char]==0:
                return False
            cc[char] -= 1

        return all( count == 0 for count in cc.values()) 

