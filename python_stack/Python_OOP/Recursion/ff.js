function floodFill(canvas, start, newColor) {
    var y = start[0];
    var x = start[1];
    var oldColor = canvas[y][x];
     // base case

    if (y < 0 || x < 0 || y >= canvas.length || x >= canvas[0].length) return;
    canvas[y][x] = newColor
   //top
    if (y > 0) {
        start = [y - 1, x] 
        if (canvas[y - 1][x] == oldColor) {
            floodFill(canvas, start, newColor, oldColor)
            
        }
    }
    //bottom
    if (y < canvas.length-1) {
        start = [y + 1, x] 
        if (canvas[y + 1][x] == oldColor) {
            floodFill(canvas, start, newColor, oldColor)
        }
    }
    //left
    if(x>0)
    {
    start=[y,x-1]
        if(canvas[y][x-1]==oldColor){
        floodFill(canvas,start,newColor,oldColor)
    }
    }
    //right
    if(x<canvas[0].length+1)
    {
    start=[y,x+1]
        if(canvas[y][x+1]==oldColor){
        floodFill(canvas,start,newColor,oldColor)
    }
    }
   return canvas;
}
canvas = [
    [3, 2, 3, 4, 3],
    [2, 3, 3, 4, 0],
    [3, 3, 3, 3, 3],
    [6, 5, 3, 4, 1]
    
];
start = [2, 2];
newColor = 1;
newCanvas = floodFill(canvas, start, newColor);
console.log(newCanvas);