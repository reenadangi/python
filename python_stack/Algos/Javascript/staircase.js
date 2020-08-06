function staircase(n) {

    for(let i=1;i<=n;i++){
        let str="";
        for(let k=i;k<n;k++){
            str=str+" ";
        }
        for(let j=0;j<i;j++){
            str=str+"#";

        }
        console.log(str)
    }

}
staircase(6);