const tree={
    a:1,
    b:1,
    c:1,
    d:{
        d1:2,
        d1:1
    }

}
function check(tree){
    let validKey=tree['a'];
    for(let key in tree){
        if(tree[key]!==validKey){
            console.log(typeof(tree[key]))
            if (typeof(tree[key]) instanceof Object){
                check(tree[key])
            }
            else{
                console.log(tree[key])
            }
            
        }
        else{
            console.log(key)
        }
        
    }
    return true
}
console.log(check(tree))