function rotateArray(a,d){
    let size=a.length;
    let rotated_array=[];
    let i=0;
    let rotateIndex=d;
    while(rotateIndex<size){
        rotated_array[i]=a[rotateIndex];
        i++;
        rotateIndex++;
    }
    rotateIndex=0;
    while(rotateIndex<d){
        rotated_array[i]=a[rotateIndex];
        i++;
        rotateIndex++;

    }
    return rotated_array;

}