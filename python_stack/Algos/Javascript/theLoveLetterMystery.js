function theLoveLetterMystery(s) {
     var count=0;
        for(var i=0,j=s.length-1; i<j; i++,j--){
       
            if(s[i]!=s[j]){
                count+=Math.abs(s.charCodeAt(i)-s.charCodeAt(j));            
            }
        }
        return count;   

}
console.log(theLoveLetterMystery("abc"))