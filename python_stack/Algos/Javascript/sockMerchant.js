// Complete the sockMerchant function below.
function sockMerchant(n, ar) {
    ar=ar.sort();
    pairs=0;
    for(let i=0;i<n-1;i++){
        
        if(ar[i]==ar[i+1]){
            pairs++;
            i++;
        }
    }
    return pairs;
}
console.log(sockMerchant(7,[1,2,1,2,1,3,2]));