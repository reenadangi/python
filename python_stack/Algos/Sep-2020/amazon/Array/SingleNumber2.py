def singleNumber( nums):
    lookup_dict = {}
    for i in nums:
        if i not in lookup_dict:
            lookup_dict[i] = 1
        else:
            if lookup_dict.get(i) == 1:
                lookup_dict[i] = 2
            else:
                lookup_dict.pop(i)
    print(lookup_dict)
    return(list(lookup_dict.keys())[0])
print(singleNumber([5,5,3,5]))