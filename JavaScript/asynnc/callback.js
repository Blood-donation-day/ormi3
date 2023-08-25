`use strict`;


// 자바스크립트는 동기적을 실행됨
//  hoisting: var, function, declaration


console.log(`1`);


// setTimeout(function () {
//     console.log(`2`);
// }, 1000);

setTimeout(() => console.log(`2`), 1000);
console.log(`3`);


function printImmediately(print) {
    print();
}

printImmediately(() => console.log(`hello`))

function printWithDelay(print, timeout) {
    setTimeout(print, timeout);
}

printWithDelay(() => console.log(`async callback`), 2000)

// 콜백 예제

class UserStorage {
    로그인유저(id, password, onSuccess, onError) {
        setTimeout(() => {
            if (
                (id === `ellie` && password ===`dream`) ||
                (id === `corder` && password ===`academy`)
            ) {
                onSuccess(id);
            } else {
                onError(new Error(`not found`));
            }
        }, 2000);
    }

    getRoles(user, onSuccess, onError) {
        setTimeout(() => {
            if (user ===`ellie`) {
                onSuccess({ name:`ellie`,role : `admin` });
            } else {
                onError(new Error(`너 admin 아니야. no access`));
            }
        }, 1000);
    }
}

const UserStorage = new UserStorage();
const id = prompt(`enter tour id`);
const password = prompt(`enter your password`);
userStorage.loginUser (
    id,
    password,
    user => {
        userStorage.getRoles(
            user,
            userwithRole => {
                alert(`Hello ${user.name}`)
            },
            error => {
                console.log(error);
            }
        );
    },
    error => {
        console.log(error);
    }
);