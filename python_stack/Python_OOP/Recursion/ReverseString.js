/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
function reverseString(str){

if (str.length<=0) return
console.log(str[str.length-1])
reverseString(str.substring(0,str.length-1))

}

reverseString("hello")