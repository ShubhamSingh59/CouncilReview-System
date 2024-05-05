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