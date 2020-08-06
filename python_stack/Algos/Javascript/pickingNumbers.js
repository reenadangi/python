function pickingNumbers(a){
   var mySet=new Set();
   var maxCount=0;
   for(var i=0;i<a.length;i++){
       var count=0;
       if (!mySet.has(a[i])){
           mySet.add(a[i])
           for(var j=0;j<a.length;j++){
               if(a[j]==a[i] || a[j]==a[i]+1){
                   count++;
               }
           }
           maxCount=Math.max(count,maxCount);
       }
   }
return maxCount;

}
console.log(pickingNumbers([4,6, 5, 3, 3, 1]))