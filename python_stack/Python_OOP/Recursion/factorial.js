//Recursive Sigma
    //Write a recursive function that
    //given a number returns the sum of integers
    //from 1 to that number.

//Example
    //recSigma(5) returns 15 
    //(5 + 4 + 3 + 2 + 1)

function recSigma(num){
    if (num<=0)
     {  return 0;
     }
    return num + recSigma(num-1)
  
}
console.log(`Recursive sum of 5: ${recSigma(5)}`)







//Recursive Factorial
    //Given num, return the product of integers
    //from 1 up to num. If less than zero,
    //return 0.

//Example
    //recFact(3) returns 6
    //(3 * 2 * 1)

    // function recFact(num,factorial){

    //     if(num<=1) {
    //         console.log(factorial)
    //         return factorial}
    //     factorial*=num
    //     console.log(factorial)
    //     recFact(num-1,factorial)

    // }
    // recFact(3,1)

 function recFact(num) 
    { 
        if (num == 0) {
          return 1}
          
        return (num*recFact(num-1)); 
    } 
    console.log(`Factorial of 3 : ${recFact(3)}`);
