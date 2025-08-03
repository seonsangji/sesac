const form = document.getElementById('validationForm')

document.getElementById('userid').addEventListener('blur', validateId);
document.getElementById('password').addEventListener('blur', validatePassword);
document.getElementById('confirm_pw').addEventListener('blur', validateConfirmPW);

function validateId() {
    const userid = document.getElementById('userid');
    userid.classList.remove('is-invalid', 'is-valid')
    if (userid.value.length < 3 || userid.value.length > 8) {
        userid.classList.add('is-invalid');
    } else {
        userid.classList.add('is-valid')
    }
};

function validatePassword() {
    const pw = document.getElementById('password');
    const lengthFeedback = document.getElementById('length_feedback');
    const patternFeedback = document.getElementById('pattern_feedback');

    pw.classList.remove('is-invalid', 'is-valid');
    lengthFeedback.classList.remove('d-block');
    patternFeedback.classList.remove('d-block');

    let validCount = 0;
    const regex = /^(?=.*[A-Za-z])(?=.*\d).+$/;

    if (pw.value.length >= 8 && pw.value.length <= 16) {
        validCount += 1;
    }

    if ( regex.test(pw.value)) {
        validCount += 2
    }

    if ( validCount === 0 ) {
        pw.classList.add('is-invalid');
        lengthFeedback.classList.add('d-block');
        patternFeedback.classList.add('d-block');
    } else if ( validCount === 1 ) {
        pw.classList.add('is-invalid');
        patternFeedback.classList.add('d-block');
    } else if ( validCount === 2) {
        pw.classList.add('is-invalid');
        lengthFeedback.classList.add('d-block');
    } else {
        pw.classList.add('is-valid')
    }
}

function validateConfirmPW() {
    const pw = document.getElementById('password');
    const confirm_pw = document.getElementById('confirm_pw');
    confirm_pw.classList.remove('is-invalid', 'is-valid');
    if ( confirm_pw.value === "" || confirm_pw.value !== pw.value ) {
        confirm_pw.classList.add('is-invalid');
    } else {
        confirm_pw.classList.add('is-valid');
    }
}
