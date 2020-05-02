def numJewelsInStones(J,S):
    return len([s for s in S if s in J ])
print (numJewelsInStones("aA","aAAbbbb"))
