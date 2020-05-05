def destCity(paths):
    source=[]
    destination=[]
    for path in paths:
        source.append(path[0])
        destination.append(path[1])
    return list(set(destination)-set(source))[0]
print (destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
