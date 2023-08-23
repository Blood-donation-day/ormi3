let test = new RegExp("aabbcc", "gi").flags;

console.log(test)   //>> gi  flag를 추출


const test2 = /aabbcc/gi.source;

console.log(test2)  // >>aabbcc source를 추출


const regexp2 = /abc/i;
console.log(regexp2.ignoreCase)

const exec_test = '글자찾기 테스트';

// ??

console.log(typeof(exec_test));
console.log(글자.exec(exec_test));