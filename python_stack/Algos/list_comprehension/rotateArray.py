def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k == n:
            return 
        nums = [nums[(i-k)%n] for i in range(n)]
        return nums
print(rotate([1,2,3,4,5,6,7,8],3))