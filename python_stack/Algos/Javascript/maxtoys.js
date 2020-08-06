function sort(prices){
   
    for(let i=0;i<prices.length;i++){
      
        for(let j=i+1;j<prices.length;j++){
                if(prices[i]>prices[j]){
                
                    let temp=prices[i]
                    prices[i]=prices[j]
                    prices[j]=temp
                }
        }
    }
    return(prices)
}
function maximumToys(prices, k) {
   prices=sort(prices)
    sum=0
    count=0
    console.log(prices)
    for(let i=0;i<prices.length;i++){
      
        if(sum+prices[i]<k){
            sum+=prices[i]
            count++;
        }
        else{
            break;
        }
    }
console.log(sum,count)

}
maximumToys([1,12,5,111,200,1000,10],50)