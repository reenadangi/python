// const person={
//     name:"reena",
//     walk(){
//         console.log(this)
//     }
// }
// const walk=person.walk.bind(person)
// walk()

// const square=(num)=>{
//     return num*10
// }
// console.log(square(12))
// const jobs=[
//     {id:1,isActive:true},
//     {id:2,isActive:false},
//     {id:3,isActive:false},
// ];
// const activeJobs=jobs.filter(job=>job.isActive
//     );
// console.log(activeJobs)


// // const person={
// //     talk(){
// //         setTimeout(function(){
// //             console.log(this)
// //         },1000);
// //     }
// // }
// // const person={
// //     talk(){
// //         setTimeout(()=>{
// //             console.log("this",this)
// //         },1000);
// //     }
// // }
// // person.talk();
//     const colors=['red','yellow','white']
//     const items=colors.map(color=>`<li>color</li>`);
//     console.log(items)

// const address={
//     street:'',
//     city:'',
//     country:''
// };
// const street=address.street
// const city=address.city
// const country=address.country
// const{street:st}=address

// const first={name:'reena'}
// const sec={city:'chicago'}
// // const combined=first.concat(sec)
// const combined={...first,...sec,language:'Python'}
// console.log(combined)


class Person{
    constructor(name){
        this.name=name;
    }
    walk(){
        console.log("walk",this.name)
    }
}
const person=new Person("reena")
person.walk()
class Teacher extends Person{
    constructor(name,dgree){
        super(name);
        this.dgree=dgree
    }
    teach(){
        console.log(this.dgree)
    }
}
const teacher=new Teacher('mosh',"CS")
teacher.teach()
teacher.walk()
