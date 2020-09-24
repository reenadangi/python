def firstMissingPositive(nums):
        s = set(nums)
        count = 1
		# starting from 1, return the first missing value
        while True:
            if count not in s: return count
            else: count += 1

print(firstMissingPositive([0,2,8,9,11,12]))