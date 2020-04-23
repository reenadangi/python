# You're given strings 'Rainbow' representing colors of rainbow, and 'C' representing the colors you have. You want to know how many rainbow colors(unique) you have.

# All characters in Rainbow and C are letters. Letters are case sensitive.

# Example 1:
# Input: Rainbow = "VIBGYOR", S = "BGgRRppw"
# Output: 3

# Example 2:
# Input: Rainbow = "VIBGYOR", S = "WW"
# Output: 0



# Rainbow = "VIBGYOR"
# S = "wwVIBBbv"
# res=[]
# [res.append(c) for c in S if c in Rainbow and c not in res ]
# print (len(res))