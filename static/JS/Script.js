function rateStar(star, inputId) {
    // Get the index of the clicked star
    const stars = star.parentNode.querySelectorAll('.fa-star');
    const starIndex = Array.from(stars).indexOf(star) + 1;

    // Update the star colors based on the index
    for (let i = 0; i < stars.length; i++) {
        if (i < starIndex) {
            stars[i].style.color = 'gold';
        } else {
            stars[i].style.color = 'aliceblue';
        }
    }

    // Update the hidden input value
    document.getElementById(inputId).value = starIndex;
}
const emailInput = document.getElementById('email');
const emailError = document.getElementById('emailError');
const passwordInput = document.getElementById('password');
const passwordError = document.getElementById('passwordError');

// Add event listeners to the input fields to validate them on input
emailInput.addEventListener('input', validateEmail);
passwordInput.addEventListener('input', validatePassword);

function validateEmail() {
    if (emailInput.validity.valid) {
        // Hide the error message if the email is valid
        emailError.style.display = 'none';
    } else {
        // Show the error message if the email is invalid
        emailError.style.display = 'block';
    }
}

function validatePassword() {
    if (passwordInput.validity.valid) {
        // Hide the error message if the password is valid
        passwordError.style.display = 'none';
    } else {
        // Show the error message if the password is invalid
        passwordError.style.display = 'block';
    }
}