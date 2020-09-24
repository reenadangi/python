def findSmallestSetOfVertices( n, edges):
        froms = set()
        to = set()
        for i in edges:
            print(i)
            froms.add(i[0])
            to.add(i[1])
        print(froms)
        print(to)
        return list(froms.difference(to))
print(findSmallestSetOfVertices(6,[[0,1],[0,2],[2,5],[3,4],[4,2]]))