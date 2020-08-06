function birthdayCakeCandles(ar) {
    let tallest=0
    let count=0
    for(let i=0;i<ar.length;i++){
        if(ar[i]>tallest){
            tallest=ar[i];
            count=1
        }
        else if(ar[i]==tallest){
            count++;
        }
    }
    return count;

}
console.log(birthdayCakeCandles([3,2,1,3]));