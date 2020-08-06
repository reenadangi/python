// Complete the jumpingOnClouds function below.
function jumpingOnClouds(c) {
    let i=0;
    let jumps=0;
    while(i+2==c.length|| i<c.length-1){
        if(c[i+2]==1){
            jumps++;
            i++;
        }
        else{
            i+=2;
            jumps++;
        }
    }
    return jumps;
}
console.log(jumpingOnClouds([0,0, 1, 0, 0, 1, 0]))