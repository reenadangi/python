function reverse(sentence){
var array=sentence.split(" ");    
var last=array.length-1;
var revSentence="";
while(last>=0){
    revSentence+=array[last]
   console.log(revSentence);
   last--;
   if(last>=0){
    revSentence+=" "}
}
return revSentence
}
var sentence="This is a test";
console.log(reverse(sentence));

