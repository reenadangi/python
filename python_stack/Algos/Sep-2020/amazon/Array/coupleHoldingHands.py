# Idea: First construct a dictionary mapping each person to the index at which he/she sits. Then we iterate over row and greedily construct the solution, i.e., for each i % 2 == 0, we swap row[i+1] with the correct person so that row[i+1] forms a couple with row[i]. The total number of such swaps is the minimum number of swaps to make the couples sit together.
# initialize: row = [0,2,4,6,7,1,3,5], dic = {0:0, 2:1, 4:2, 6:3, 7:4, 1:5, 3:6, 5:7}
# i = 0: row = [0,1,4,6,7,2,3,5], dic = {0:0, 1:1, 4:2, 6:3, 7:4, 2:5, 3:6, 5:7}
# i = 2: row = [0,1,4,5,7,2,3,6], dic = {0:0, 1:1, 4:2, 5:3, 7:4, 2:5, 3:6, 6:7}
# i = 4: row = [0,1,4,5,7,6,3,2], dic = {0:0, 1:1, 4:2, 5:3, 7:4, 6:5, 3:6, 2:7}
# i = 6: row = [0,1,4,5,7,6,3,2], dic = {0:0, 1:1, 4:2, 5:3, 7:4, 6:5, 3:6, 2:7}
def minSwapsCouples(row):
    dic = {x:i for i,x in enumerate(row)}
    res = 0
    for i, n in enumerate(row):
        if i % 2 == 0:
            if n % 2 == 1:
                if row[i+1] != n-1:
                    tmp = dic[n-1]
                    row[dic[n-1]], row[i+1] = row[i+1], row[dic[n-1]]
                    dic[row[i+1]] = i+1
                    dic[row[tmp]] = tmp
                    res += 1
            else:
                if row[i+1] != n+1:
                    tmp = dic[n+1]
                    row[dic[n+1]], row[i+1] = row[i+1], row[dic[n+1]]
                    dic[row[i+1]] = i+1
                    dic[row[tmp]] = tmp
                    res += 1
    return res