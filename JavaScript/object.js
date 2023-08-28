//
//이름과 나이를 지정하고 이름과 나이를 출력하는 함수를 만들고 그 함수를 사용하여 출력
// 길어지고 가독성 떨어짐
const name = `chang`;
const age = 21;

print(name,age);

function print(name,age){
console.log(name);
console.log(age);
}

// 오브젝트 = { key: value, key2 : value2 ...}

const chang = {name:`chang`, age: 21};

function prints(chang){
    console.log(chang.name);
    console.log(chang.age);
    }

prints(chang);

chang.job = `student`
console.log(chang)

// const object1 = {}  //     `object literal` syntax
// const object2 = new {}  // `object constructor` syntax  



//computed properties

console.log(chang.job);   // properties 를 불러오는 방법 2개.
console.log(chang[`job`]); //  string type으로 해야 불러와짐. 

function properties (key, val) {
    console.log(key[val])
};

properties(chang, `age`);


// property value shorthand

const person1 = {name:`chang`, age:23,}; 
const person2 = {name:`hwan`, age:17,}; 
const person3 = {name:`kim`, age:48,}; 
const person4 = new Addperson (`kkiimm`, 12);
console.log(person4)

// function addperson(name, age) {
//     return {
//         name, age,
//     };
// };

function Addperson (name, age) {
    this.name = name;
    this.age = age;
};

//for ... in  // for...of

// for (key in value) {
//     console.log(key);
// }

const ary = [[1, 2], [3, 4]];
for (value of ary) {   //잘라서 한바퀴 돌음 value로 출력
    console.log(value);
}


