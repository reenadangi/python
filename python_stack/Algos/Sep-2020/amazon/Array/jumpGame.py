#       
def jump(nums):
        currdes,step,des=0,0,0
        for i in range(len(nums)-2):
            des=max(des,i+nums[i])
            if currdes==i:
                currdes=des
                step+=1
        return step
print(jump([2,1,3,1,4]))