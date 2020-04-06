def groupAnagrams(strs):
    new_dict = {}
    for i in range(0,len(strs)):
            element = tuple(sorted(strs[i]))
            if element in new_dict:
                new_dict[element].append(strs[i])
            else:
                new_dict[element] = [strs[i]]
                
    return new_dict.values()        
    
 
  
   

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
