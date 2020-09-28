def findLucky(arr):
        # dic={}
        # for i in range(len(arr)):
        #     if arr[i] in dic:
        #         dic[arr[i]]=dic[arr[i]]+1
        #     else:
        #         dic[arr[i]]=1
        # lst=[]
        # for n in dic:
        #     if dic[n] == n: 
        #         lst.append(n)
        #         # res = max(res, )
        # if lst:
        #     return(max(lst))
        # return -1
        
        lucky = []
        for i in arr:
            if arr.count(i) == i:
                lucky.append(i)
                
        if len(lucky) == 0:
            return - 1
        
        else:
            lucky.sort()
            return lucky[len(lucky)-1]
      
      
        


                
print(findLucky([1,2,2,3,3,3]))
      