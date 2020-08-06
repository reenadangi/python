function icecreamParlor(m, arr) {
        //Search each combination of 2 nos. to check if the sum is equal to the total money and then print the indexs+1. 
for(var i=0;i<arr.length-1;i++){
    for(var j=i+1;j<arr.length;j++){
        if(arr[i]+arr[j]==m){
            return ((i+1)+" "+(j+1));
        }
    }
}
}
console.log(icecreamParlor(6,[1,3,4,5,6]))
