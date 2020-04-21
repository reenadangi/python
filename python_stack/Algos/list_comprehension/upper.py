lst=['banana ','tomato','potato','kiwi']
lst=[s[0].upper()+s[1:] for s in lst]
print (lst)
lst=[s.strip() for s in lst]
print (lst)