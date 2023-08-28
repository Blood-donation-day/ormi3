const num3 = [13, 9, 10];
const 숫자배열 = [71,600,1879,54,42,87,900,122]


숫자배열.sort(function (a, b) {
  console.log(`a: ${a}` , `b: ${b}`);
  return a - b;
});

function 바보상자(a , b) {
  return a - b;
}


// 숫자배열.sort(바보상자);

// console.log(숫자배열);

// [71,600,1879,54,42,87,900,122]
// 0   a: 600 b: 71
// 1   a: 1879 b: 600
// 2   a: 54 b: 1879
// 3   a: 54 b: 600
// 4   a: 54 b: 71
// 5   a: 42 b: 600
// 6   a: 42 b: 71
// 7   a: 42 b: 54
// 8   a: 87 b: 71
// 9   a: 87 b: 1879
// 1   a: 87 b: 600
// 11  a: 900 b: 87
// 12  a: 900 b: 1879
// 13  a: 900 b: 600
// 14  a: 122 b: 87
// 15  a: 122 b: 900
// 16  a: 122 b: 600



// 첫번째는 0 1 양수 음수를 비교
//         1 2 양수 음수 
//         2 3 여기서 음수나옴.  54 < > 1879
//         2 1 음수             54 < > 600
//         2 0 음수             54 < > 71  ... 반복 정렬
        
                     


let result = 숫자배열.reduce((a, b ) => {
  return a + b
}, 0); 

console.log(result);


// 배열 내용 복습
const fruit = [`apple`, `melon`, `banana`];

for (type of fruit) {
  console.log(type);
};

for (i=0; i<fruit.length; i++) {
  for (j = 0; j < 7; j++) {
    console.log(fruit[i][j]);
  }  
};

fruit.forEach((fruit, index) => console.log(fruit, index) );

const fruit2 = [`사과`, `멜론`, `바나나`];
const fruit3 = fruit.concat(fruit2);
console.log(fruit3);

const finder = (name) => console.log(`찾고 계신 ${name}은 ${fruit3.indexOf(name) + 1}번째에 있습니다.`)
function search (ary, name) {
  if (ary.includes(name)) {
    console.log(`찾고 계신 ${name}은 ${ary.indexOf(name) + 1 }번째에 있습니다.`)
  } else {
    console.log(`해당 과일을 찾을 수 없습니다.`)
  }
}

finder(`바나나`)
search(fruit2, `멜론`)  //찾는 과일이 없는 경우 추가

