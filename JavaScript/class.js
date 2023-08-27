`use strict`

//class : template
//object : 

//클래스 선언
class Person {
    //constructor
    constructor(name, age) {
        //fields
        this.name = name;
        this.age = age;
    }
   

    //methods
    speak() {
        console.log(`${this.name}: hello~`);
    };
};


const 사용자이름 = new Person(`chang`, 20);
console.log(사용자이름.name);
console.log(사용자이름.age);


// 2. getter & setters     
//  this.age = age;  에서 왼쪽 불러올때 getter    오른쪽 setter 호출
class User {
    constructor (name, phone ,age) {
        this.name = name;
        this.phone = phone;
        this.age = age;
    };

    get age() {
        return this._age;
    }


    set age(value_age) {
        if (value_age < 0 ) {
            console.log(`나이는 음수가 될 수 없습니다!`)
            return 0;
        }
        this._age = value_age;
    }
};

const user1 = new User (`chang`, 6415, -1);
console.log(user1.age);

//3.fields (public, private)

class test {
    publicfield = 2;
    #privatefield = 0;

};

const testt = new test;
console.log(test.publicfield);
// console.log(test.#privatefield);  // privatefield 는 클래스 안에서만 호출, 변경가능

// 4. statics

class Coffee {
    
    static from = `korea`;
    constructor(coffeegrade) {
        this.coffeegrade = coffeegrade;
    }
    
    static startmaking() {
        console.log(Coffee.from);
    }
}

const coffee1 = new Coffee(1);
const coffee2 = new Coffee(2);
console.log(Coffee.from); //
Coffee.startmaking();  //

//상속

class Shape {
    constructor(width, height, color) {
        this.width = width;
        this.height = height;
        this.color = color;
    }

    draw () {
        console.log(`drawing ${this.color} color of`);
    }

    getArea () {
        return this.width * this.height;
    }
}

class Rectangle extends Shape {}  // Shape의 내용을 Rectangle class 가 따라감.
class Triangle extends Shape {
    getArea () {
        return (this.width * this.height) / 2 ;
    }
}  // Shape의 내용을 Rectangle class 가 따라감. 추가로 내용 변경


const rectangle = new Rectangle(20,20, `blue`);
const triangle = new Triangle(20,20, `blue`);


rectangle.draw();
console.log(rectangle.getArea());
console.log(triangle.getArea());


//instanceOf   왼쪽이 오른쪽에 있는거에 의해 만들어진게 맞는지 

console.log(rectangle instanceof Rectangle);