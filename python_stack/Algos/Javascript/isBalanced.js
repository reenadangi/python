function isBalanced(s) {
   let mystack=[] 
   let mapping={')':'(','}':'{',']':'['}
for(let i=0;i<s.length;i++){
   
    if(s[i]=='('||s[i]=='{'||s[i]=='['){
        mystack.push(s[i])
    }
    else if(s[i]==')'||s[i]=='}'||s[i]==']'){
        if(mystack){
            pop_val=mystack.pop();
            if(s[i]==")" && pop_val!="("){
                return "No";
            }
            else if(s[i]=="}" && pop_val!="{"){
                return "No";
            } 
            else if(s[i]=="]" && pop_val!="["){
                return "No";
            }   

        }
        else{
            return "No";
        }
        
    }
   
}
if(mystack.length>0){
    return "No";
}else{
    return "Yes";
}
}
console.log(isBalanced('{[()]}'))