def search(nums,value):
    for i in nums:
        if i==value:
            return True
    return False
print(search([4,5,6,8],80))