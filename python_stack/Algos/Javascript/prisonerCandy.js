function saveThePrisoner(n, m, s) {
    var r=m %n;
    if((r+s -1)%n==0){
        return n;
    }
    else{
        return((r+s-1)%n);
    }
}
console.log(saveThePrisoner(7,19,2))
