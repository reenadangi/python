# Given two strings s and t , write a function to determine if t is an anagram of s.
# Input: s = "anagram", t = "anagram"
# Output: true
def isAnagram(s, t):
    if sorted(s)!=sorted(t):
        return False
    return True
  


    
print(isAnagram("ac","bb"))

