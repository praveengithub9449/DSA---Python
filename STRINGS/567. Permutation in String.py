# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# class Solution(object):
#     def permutation(self,s1,s2):

from collections import Counter 
def per(s1,s2):
    

    s=Counter(s1)
   
    
    window_count= Counter(s2[:len(s1)])
    
    if s==window_count:
        return True

    for i in range (len(s1),len(s2)):
        window_count[s2[i]] += 1
    
        # print("----------------------------")
        window_count[s2[i-len(s1)]] -= 1
       

        if window_count[s2[i-len(s1)]] ==0:
            del window_count[s2[i-len(s1)]]


        if s == window_count:
            return True
    return  False
        
s1 = "ab"
s2 = "eidbaooo"       
print(per(s1, s2))

