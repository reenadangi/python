function minimumDistances(a) {
    // Find the matching element starting from the adjacent index and then calculate the distance of the indexes.Print the minimum distance.
        var dist=0;
        var minDist=Number.MAX_VALUE;
      
        for(var i=0;i<a.length;i++){
            for(var j=i+1;j<a.length;j++){
                if(a[i]==a[j]){
                    var dist=j-i;
                    minDist=Math.min(dist,minDist);
                    break;
                }
            }
        }
        if(minDist==Number.MAX_VALUE){
            return -1;
        }
        return minDist;
    }
    console.log(minimumDistances([7,1,3,4,1,7]));