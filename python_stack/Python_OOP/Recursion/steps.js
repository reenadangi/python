
function steps(n){
for(let row=1;row<n;row++)
{ let print=""
    for(col=row;col>0;col--)
    {
        print=print+"#"
   
    }
    console.log(print)
}
}
steps(3)
// #
// ##
// ###