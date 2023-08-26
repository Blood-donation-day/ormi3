//반복문 while, for 연습장

let a;


console.log(`my ` + `name`); // string +string
console.log(`12` + 1);   //number 가 string으로 바뀌고 string 끼리 더해져서 121출력

let b = 1;
const bup = b++;
// const upb = ++b;
// console.log(upb);

console.log(b);
console.log(bup);



let x =3;
let y = 6;

console.log(`x의 시작값은 "${x}" 입니다.`);
x += y;
console.log(`현재 x의 값은 ${x}입니다.`);
x -= y;
console.log(`현재 x의 값은 ${x}입니다.`);
x /= y;
console.log(`현재 x의 값은 ${x}입니다.`);
x *= y;
console.log(`현재 x의 값은 ${x}입니다.`);



// || (or)     && (and)    ! () not


function checknumber(check1) {
    for (i=0; i<5; i++) {
        if ( check1 < 5) {
            console.log(`현재 x 의 값은 ${x}임으로 5보다 작습니다.`)
            
        } else {
            console.log(`현재 x 의 값은 ${x}임으로 5보다 큽니다.`)
        }
        
    };
    return;
};

const value1 = true;
const value2 = 1;

console.log(`or : ${value1 || value2 || checknumber(x)}`) 
//함수 등 시간이 오래걸리는 작업은 뒤로 보내서 체크하는 시간을 줄여야 한다.

console.log(`not 연산자는 반대로 츨력임으로 true가 ${!value1}로 바뀐다.`)

const 닉네임1 = {name: `nickname`};
const 닉네임2 = {name: `nickname`};
const 닉네임3 = 닉네임1;

console.log(닉네임1 == 닉네임2);  //다른 ref이으로 false   ==은 타입을 건너뛸 수 있음
console.log(닉네임1 === 닉네임2); //마찬가지로 서로다른 ref이므로 false
console.log(닉네임1 === 닉네임3); // 서로 같음 >> true


console.log(닉네임1 === `nickname` ? `nick이네` : `nick이 아니잔아 `)
// 상태 ? true일때 : false 일때

//if 에서 elseif 쓸게 너무 많아지면 swich사용하자 

const 게임종류 = {선택 : `FPS`}


switch (게임종류.선택) {
    case `FPS`:
        console.log(`fps는 주로 총으로 하는 게임입니다.`);
        break;
    case `RPG`:
        console.log(`RPG는 캐릭터를 키우는 게임입니다.`);
        break;
    case `AOS`:
        console.log(`AOS는 캐릭터를 키우는 게임입니다.`);
        break;
    default:
        console.log(`장르 밖의 게임입니다.`);
        break;
};



    for (i = 0; i < 0; i++){
        while ( i > 0 ) {
            console.log(`while: ${i}`)
            i--;
        }
    }

//do while에서는 while조건에 맞지 않더라도 한번의 실행을 보장함.
do {
    console.log(`do while: ${i}`)
} while ( i > 0 );


// for ( begin; condition; step)
//이중 for : 권장되지 않음
for (let i =0; i < 10; i++) {
    for (let j = 0; j < 10; j++){
        console.log(`i:${i} and j:${j}`)
    }
}


// break, continue 
// 짝수만 출력


for (i=0; i<11; i++) {
    if ( i % 2 === 0) {
        continue;
    }
    console.log(`i의 값은 ${i}입니당`)
};


for (i=0; i<11; i++) {
    if ( i > 8) {
        break;
    } else {
    console.log(`i의 값은 ${i}입니당`)
    };
};

