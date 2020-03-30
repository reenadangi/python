# Selection Sort

# Find the minimum element in arr[0...4]
#  and place it at beginning
# 11 25 12 22 64
my_arr = [5,2,3,1] 
def sort(nums):
    for i in range(len(nums)):
        min_index=i
        for j in range(i+1,len(nums)):
            if nums[min_index]>nums[j]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]

sort(my_arr)
print(my_arr)