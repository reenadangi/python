function floodFill(canvas, start, newColor){
// base case
console.log(`start${start}`)
var y=start[0];
var x=start[1]; 
// if(y<0||x<0||y>canvas[0].length||x>canvas.length) return;

if(canvas[y][x]==newColor || canvas[y][x]<0 ||y<0||x<0){return}
// start=[2,2];

const oldColor=canvas[y][x]
console.log(`Old color: ${oldColor}`)
canvas[y][x]=newColor
// top
console.log(`y-1 ${y-1}, x: ${x}`)
if(canvas[y-1][x]===oldColor){
start=[[y-1],[x]]
console.log("Change top")
console.log(canvas)
floodFill(canvas,start,newColor)
}
//bottom
if(canvas[y+1][x]===oldColor){
    start=[[y+1],[x]]
    console.log("Change bottom")
    console.log(canvas)
    floodFill(canvas,start,newColor)
}


return canvas;
}
canvas= [[3, 2, 3, 4, 3],
        [2, 3, 3, 4, 0],
        [7, 3, 3, 5, 3],
        [6, 5, 3, 4, 1],
        [1, 2, 3, 3, 3]] ;
start=[2,2];
newColor=1;
newCanvas=floodFill(canvas, start, newColor);
console.log(newCanvas);

//Given 2D Canvas of:
        // [[3, 2, 3, 4, 3],
        //  [2, 3, 3, 4, 0],
        //  [7, 3, 3, 5, 3],
        //  [6, 5, 3, 4, 1],
        //  [1, 2, 3, 3, 3]]
    //Start of:
        // [2,2]
    //newColor of:
        // 1
    
         //2D Canvas Becomes:
        // [[3, 2, 1, 4, 3],
        //  [2, 1, 1, 4, 0],
        //  [7, 1, 1, 5, 3],
        //  [6, 5, 1, 4, 1],
        //  [1, 2, 1, 1, 1]]
