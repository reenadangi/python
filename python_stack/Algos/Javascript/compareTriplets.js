function compareTriplets(a,b){
    let mySet=[0,0]
    for(let i=0;i<a.length;i++){
        if (a[i]!=b[i])
        {
        if(a[i]>b[i]){
            mySet[0]=mySet[0]+1
        }
        else{
            mySet[1]=mySet[1]+1
        }
    }
        
    }
    console.log(mySet);
    
}
compareTriplets([1, 28, 30],[99, 16, 8])