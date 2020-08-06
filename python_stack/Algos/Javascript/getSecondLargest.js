function getSecondLargest(nums){
    let max=nums[0];
    let secLargest=0;
    for(let i=1;i<nums.length;i++){
        if(nums[i]>max){
            secLargest=max;
            max=nums[i];
        }
        else if(nums[i]>secLargest && nums[i]<max){
            secLargest=nums[i];
        }
    }
    console.log("largest", max);
    console.log("Seclargest", secLargest);
}
getSecondLargest([2, 3, 6, 6, 5]);
