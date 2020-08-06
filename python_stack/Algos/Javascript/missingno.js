// Complete the missingNumbers function below.
function missingNumbers(arrA, arrB) {
    var freq=0;
    var freqInA=0;
    var distArrB=[];
    var missingNos=[];
    var n=arrA.length;
    var m=arrB.length;
    
   arrB.sort(function(a,b){return a-b});
    
    distArrB= arrB.slice();
    for(var i=0; i<distArrB.length-1; i++){
        for(var j=i+1; j<distArrB.length; j++){
            if(distArrB[i]==distArrB[j]){
                distArrB.splice(j,1);
                j--;
            }
        }      
    }
    
    for(var i=0; i<distArrB.length; i++){
        for(var j=0; j<m; j++){           
            if(distArrB[i]==arrB[j]){
                freq++;
            }           
        }
        
        for(var k=0; k<n; k++){
            if(distArrB[i]==arrA[k]){
                freqInA++;
            }
        }
        if(freq!=freqInA){
            missingNos.push(distArrB[i]);
        }
        freq=0;
        freqInA=0;
    }
    
    var str=missingNos.join(" ");
    return str;
} 
 

   


console.log(missingNumbers([203,204,205,206,207,208,203,204,205,206],[203,204,204,205,206,207,205,208,203,206,205,206,204]));