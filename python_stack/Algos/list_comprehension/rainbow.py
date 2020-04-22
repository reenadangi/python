# You're given strings 'Rainbow' representing colors of rainbow, and 'C' representing the colors you have. You want to know how many unique rainbow colors you have.

# All characters in Rainbow and C are letters. Letters are not case sensitive, so "v" is considered same as "V".

# Example 1:
# Input: Rainbow = "vibgyor", S = "BGgRppw"
# Output: 3

# Example 2:
# Input: Rainbow = "vibgyor", S = "WW"
# Output: 0

Rainbow = "vibgyor"
S = "ww"
res=[]
res=[c for c in S if c.upper() in Rainbow.upper() and c not in res ]
print(len(res))