/**
 * DOM elements for the registration page
 */
const homeArea = document.querySelector('.home_area');
const signUpButton = document.querySelector('.sign_up_button');
const registrationArea = document.querySelector('.registration_area');

/**
 * Event handler for the "Sign Up" button on the home page click.
 * Displays registration form on click
 */
signUpButton.onclick = () => {
    console.log('Sign Up Button clicked');
    registrationArea.classList.add('active');
    homeArea.classList.add('active');
};
