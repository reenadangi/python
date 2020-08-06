class Polygon {
    constructor(sides) {
        this.sides = sides;
      }
      perimeter(){
        let sum=0;
        for(let i in this.sides)
        {
            sum+=this.sides[i];
        }
        return(sum)
      }
      
    
}
