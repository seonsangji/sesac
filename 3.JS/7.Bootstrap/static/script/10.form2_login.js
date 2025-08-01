const form = document.getElementById('validationForm');

document.getElementById('id').addEventListener('blur', validateId);
document.getElementById('password').addEventListener('blur', validatePassword);
document.getElementById('username').addEventListener('blur', validateUsername)
document.querySelectorAll('.form-check').forEach(checkbox => {
    checkbox.addEventListener('change', validateInterest)
})

function validateId() {
    const id = document.getElementById('id');
    id.classList.remove('is-invalid', 'is-valid')
    if (id.value.length < 3 || id.value.length > 10) {
        id.classList.add('is-invalid');
    } else {
        id.classList.add('is-valid')
    }
};

function validatePassword() {
    const password = document.getElementById('password');
    const tooShort = document.getElementById('too-short-feedback');
    const noPattern = document.getElementById('no-pattern-feedback');
    const Value = password.value;

    
    const satisfyingPattern =
    /[A-Za-z]/.test(Value) &&
    /[0-9]/.test(Value) &&
    /[^A-Za-z0-9]/.test(Value);
    
    password.classList.remove('is-valid', 'is-invalid');
    
    let passwordCharTypeCount = 0;

    if (Value.length >= 8) {
        passwordCharTypeCount += 1
    } 

    if (satisfyingPattern) {
        passwordCharTypeCount += 2
    } 

    if (passwordCharTypeCount === 3) {
        password.classList.add('is-valid')
    } else if (passwordCharTypeCount === 2) { 
        // 자릿수 만족 x, 문자조건 o -> tooShort 오류메시지
        password.classList.add('is-invalid');
        noPattern.classList.remove('d-block');
        tooShort.classList.remove('d-none');
        tooShort.classList.add('d-block');
    } else if (passwordCharTypeCount === 1) {
        password.classList.add('is-invalid')
        tooShort.classList.remove('d-block')
        noPattern.classList.add('d-block')
    } else {
        password.classList.add('is-invalid')
        tooShort.classList.add('d-block')
        noPattern.classList.add('d-block')
    }
}

function validateUsername() {
    const username = document.getElementById('username');
    username.classList.remove('is-invalid', 'is-valid')
    if (username.value.length == 0 || username.value.length > 10) {
        username.classList.add('is-invalid');
    } else {
        username.classList.add('is-valid')
    }
};

function validateInterest() {
    const boxes = document.querySelectorAll('.form-check');
    const selectedBoxes = Array.from(boxes).filter(checkbox => checkbox.checked);
}
