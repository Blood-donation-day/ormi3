// 산술연산
console.log(`10 + 3 = ${10 + 3}`)
console.log(`10 - 3 = ${10 - 3}`)
console.log(`10 / 3 = ${10 / 3}`)
console.log(`10 * 3 = ${10 * 3}`)
console.log(`10 ** 3 = ${10 ** 3}`) // 10의 3승
//console.log(`4 ** 0.5 = ${4 ** 0.5}`) // 4의 제곱근
console.log(`10 % 3 = ${10 % 3}`) // 나머지

// 단항연산 
console.log(-2)
console.log(-(-2))
// console.log(--2) // error
console.log(+4)
console.log(+'4')
// 소숫점 제거
// 비트연산자에서 한 번 더 해드리겠습니다.
console.log(~~3.14)

// 증감연산자
let num = 3; // 증감연산자는 할당연산자를 통해 할당된 값에만 사용 가능합니다.
console.log("증감연산 : ", ++num); // 4
console.log("증감연산 : ", num++); // 5 (출력하고 나서 연산을 합니다!)
console.log("증감연산 : ", --num); // 4
console.log("증감연산 : ", num--); // 3 (출력하고 나서 연산을 합니다!)
// why? 출력해보니 다 4로 출력이 될까요? 답은 증감연산자에 위치에 있습니다. 그러나 여러분들이 이 증감연산자에 위치를 고려하실 필요는 실무에서 거의 발생하지 않습니다.
// 아래 둘 다 0 ~ 9까지 출력합니다.
for (let i = 0; i < 10; ++i) {
    console.log(i)
}
for (let i = 0; i < 10; i++) {
    console.log(i)
}

// 비교연산자(값은 boolean으로 반환됩니다.)  True False => boolean
console.log("비교연산 : ", 2 > 3);
console.log("비교연산 : ", 2 >= 3);
console.log("비교연산 : ", 2 < 3);
console.log("비교연산 : ", 2 <= 3);
console.log("비교연산 : ", 2 == 3); 
console.log("비교연산 : ", 2 === 3);
// 등호 2개를 권하지 않습니다. 실무에서는 등호 3개를 사용하시길 권해드립니다.
console.log("비교연산 : ", 2 == '2'); // 다른 언어에서는 false, js에서는 true
console.log("비교연산 : ", 2 === '2'); // 다른 언어에서 이런 문법이 없고, js에서는 false