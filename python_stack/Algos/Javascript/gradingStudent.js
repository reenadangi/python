function gradingStudents(grades) {
    // Write your code here
    let res=[]
    for(let i=0;i<grades.length;i++){
        console.log(grades[i] % 5);
        if(grades[i]>=38 && grades[i] % 5 >2)
        {
            grades[i] = grades[i] + (5 - (grades[i] % 5));

        }
    }
    return(grades);

}
console.log(gradingStudents([73,67,38,33]));
