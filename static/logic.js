console.log("hello world");

// --- MODAL AND SCROLL ---
const signinUpBox = document.getElementById("signin-up-box");
const loginBox = document.getElementById("login-box");
const signupBox = document.getElementById("signup-box");
const showSignupBtn = document.getElementById("show-signup");
const showLoginBtn = document.getElementById("show-login");
const closeBtns = document.querySelectorAll(".close-btn");

// Function to disable scroll on the body
function disableScroll() {
    document.body.classList.add('noscroll');
}

// Function to enable scroll on the body
function enableScroll() {
    document.body.classList.remove('noscroll');
}

// Switch from Login to Signup form
showSignupBtn.addEventListener("click", (e) => {
    e.preventDefault();
    loginBox.classList.add("hidden");
    signupBox.classList.remove("hidden");
});

// Switch from Signup to Login form
showLoginBtn.addEventListener("click", (e) => {
    e.preventDefault();
    signupBox.classList.add("hidden");
    loginBox.classList.remove("hidden");
});

// --- PROFILE CIRCLE LOGIC ---
// Set to `false` to test the "not logged in" flow, or `true` for the "logged in" flow.
let isLoggedIn = false; 
const profileCircle = document.getElementById('profile-circle');
const profileMenu = document.getElementById('profile-menu');

profileCircle.addEventListener('click', (e) => {
    e.stopPropagation(); // Prevents the document click listener from firing immediately
    if (isLoggedIn) {
        // If logged in, toggle the profile dropdown menu
        profileMenu.classList.toggle('hidden');
    } else {
        // If not logged in, show the signin/signup modal and disable page scroll
        signinUpBox.classList.remove('hidden');
        disableScroll();
    }
});

// Event listeners for both close buttons
closeBtns.forEach(btn => {
    btn.addEventListener("click", (e) => {
        e.preventDefault();
        signinUpBox.classList.add("hidden");
        enableScroll();
    });
});

// Hide dropdown if clicked outside
document.addEventListener('click', (e) => {
    // Hide dropdown if it's open and the click is outside
    if (!profileMenu.classList.contains('hidden') && !profileCircle.contains(e.target)) {
        profileMenu.classList.add('hidden');
    }
});