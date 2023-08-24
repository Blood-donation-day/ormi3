const homework = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function 홀짝분리기(int) {
    let 홀짝판별기;
    if (int%2===1){
        홀짝판별기 = "홀수"
    }else {
        홀짝판별기 = "짝수"
    }
    return 홀짝판별기
};

console.log(homework.map(홀짝분리기)); // 홀짝 결과 
const 홀수만 = homework.filter(num => 홀짝분리기(num) === "홀수"); // 홀수로 이루어진 출력
const 홀수합계 = 홀수만.reduce((a, b) => a+b, 0);  //reduce로 `홀수만` 더하기

console.log(홀수만);
console.log(`홀수들의 합은 ${홀수합계}입니다.`);



//더 짧게 수정.

function 홀수합치기함수(a,b) {
    
    if ( b % 2 === 1) {
        return a + b;
    } else {
        return a;
    };
};

const 홀수합 = homework.reduce(홀수합치기함수, 0) ;
console.log(`답은 "${홀수합}" 입니다.`);


//더더 짧게 수정

console.log(`답은 "${homework.reduce((a, b) => 
{
    if (b % 2 === 1) {
        return a + b;
    } else {
        return a;
    }
}, 0)}" 입니다.`);