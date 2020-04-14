def stringShift(s,shift):
        move = 0
        for x, y in shift:
            if x == 0:
                # right rotation
                move -= y
            else:
                # left rotation
                move += y
        move %= len(s)
        return s[-move:] + s[:-move]

# print(stringShift("abcdefg",[[1,1],[1,1],[0,2],[1,3]]))
print(stringShift("abc",[[0,1],[1,2]]))
# print(stringShift("mecsk",[[1,4],[0,5],[0,4],[1,1],[1,5]]))
# print(stringShift("xqgwkiqpif",[[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]))
# print(stringShift("joiazl",[[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]]))


# "xqgwkiqpif"
