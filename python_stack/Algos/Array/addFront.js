function addFront(arr){
    // add in front and remove no item
    arr.splice(0,0,9)
    // or you can use unshift method   
    arr.unshift(12) 
    console.log(arr)
    for(i=arr.length;i>=0;i--){
        arr[i]=arr[i-1]
    }
    arr[0]=40
    console.log(arr)


}

addFront([1,2,3,4,5])

var fruits = ["Banana", "Orange", "Apple", "Mango"];
// At position 2, add the new items, and remove 1 item:
fruits.splice(2, 1, "Lemon", "Kiwi");
console.log(fruits)


var obj={
    a:1,
    b:1,
    c:{
        c1:1,
        c2:1
    }
}
function CheckObject(){
    
}