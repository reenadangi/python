    // Complete the luckBalance function below.
function luckBalance(k, contests) {
    contests.sort(function(a,b){
        return b[0]-a[0]
      })
      let luckBalance=0;
      for(let i=0;i<contests.length;i++){
          let luck=contests[i][0];
          let importance=contests[i][1];
          if(importance==1 && k>0){
              k--;
              luckBalance+=luck;
          }
          else if(importance==1 && k==0){
            //   no loger able to loose
            luckBalance-=luck
          }
          if(importance==0){
              luckBalance+=luck;
          }
      }
    return luckBalance;


}
let items= [[5,1],[2,1],[1,1],[8,1],[10,0],[5,0]]
console.log(luckBalance(3,items));