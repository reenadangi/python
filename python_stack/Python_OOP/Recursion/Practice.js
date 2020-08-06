function countDown(startpoint){
    if(startpoint==0) return;
    console.log(startpoint)
    countDown(startpoint-1)
}
countDown(12)

