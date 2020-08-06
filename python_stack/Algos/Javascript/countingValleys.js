// Complete the countingValleys function below.
function countingValleys(n, s) {
    let altitude=0;
    let num_valleys=0;
    for(let i=0;i<n;i++){
       
        if(s[i]=="U"){
            console.log(altitude)
            if(altitude==-1){
                num_valleys++;
            }
            altitude++;
        }
        if(s[i]=="D"){
            altitude--;
        }
    }
return num_valleys;
}
console.log(countingValleys(8,"UDDDUDUU"))
