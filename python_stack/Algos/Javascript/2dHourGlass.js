// Given a  2D Array, :

// 1 1 1 0 0 0
// 0 1 0 0 0 0
// 1 1 1 0 0 0
// 0 0 0 0 0 0
// 0 0 0 0 0 0
// 0 0 0 0 0 0
// We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

// a b c
//   d
// e f g
// There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

// For example, given the 2D array:

// -9 -9 -9  1 1 1 
//  0 -9  0  4 3 2
// -9 -9 -9  1 2 3
//  0  0  8  6 6 0
//  0  0  0 -2 0 0
//  0  0  1  2 4 0
// We calculate the following  hourglass values:

// -63, -34, -9, 12, 
// -10, 0, 28, 23, 
// -27, -11, -2, 10, 
// 9, 17, 25, 18
function hourGlassSum(arr){
    let rows=arr.length;
    let colums=arr[0].length;
    let max_sum=-63;
    for(let i=0;i<rows-2;i++){
        for(let j=0;j<colums-2;j++){
            let sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+
                            arr[i+1][j+1]+
                    arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
            max_sum=Math.max(max_sum,sum);
        }
    }
    return max_sum;
}