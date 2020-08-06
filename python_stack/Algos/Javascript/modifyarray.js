function modifyArray(nums) {
    return nums.map(n => (n%2) ? n*3 : n*2);

    
}
console.log(modifyArray([1,2,3,4]))