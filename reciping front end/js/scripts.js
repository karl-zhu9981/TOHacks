/*!
* Start Bootstrap - Resume v6.0.3 (https://startbootstrap.com/theme/resume)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE)
*/

var firebaseConfig = {
    apiKey: "AIzaSyBtm9YJpSf0tQ8cGU3S5bBY2bbxu8U0W2U",
    authDomain: "personal-info-2dbde.firebaseapp.com",
    databaseURL: "https://personal-info-2dbde-default-rtdb.firebaseio.com",
    projectId: "personal-info-2dbde",
    storageBucket: "personal-info-2dbde.appspot.com",
    messagingSenderId: "324805094921",
    appId: "1:324805094921:web:a91ddb614ea1ad5c3ed2d8",
    measurementId: "G-93BDRZLE8H"
  };
firebase.initializeApp(firebaseConfig);
firebase.analytics();

// Reference messages collection
var messagesRef = firebase.database().ref("messages");


(function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using anime.js
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').on('click', function () {
        if (
            location.pathname.replace(/^\//, "") ==
            this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length ?
                target :
                $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                anime({
                    targets: 'html, body',
                    scrollTop: target.offset().top,
                    duration: 1000,
                    easing: 'easeInOutExpo'
                });
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").on('click', function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#mainNav"
    });

})(jQuery); // End of use strict

// Listen for form submit
document.getElementById('personalInfo').addEventListener('submit', submitForm);
document.getElementById('ingredients').addEventListener('submit1', submitIngredients);

// Submit form
function submitForm(e) {
    e.preventDefault();

    // Get values
    var fname = getInputVal('fname'); // var matches up w/ getInputVal
    var fmail = getInputVal('fmail');
    var fphone = getInputVal('fphone');

    // Save message
    saveMessage(fname, fmail, fphone);

}

// Submit form
function submitIngredients(e) {
    e.preventDefault();

    // Get values
    var fingred1 = getInputVal('fingred1'); // var matches up w/ getInputVal
    var fingred2 = getInputVal('fingred2');
    var fingred3 = getInputVal('fingred3');
    var fingred4 = getInputVal('fingred4');
    var fingred5 = getInputVal('fingred5');

    // Save message
    saveMessage(fingred1, fingred2, fingred3, fingred4, fingred5);

}

// Function to get getform values
function getInputVal(id){
    return document.getElementById(id).value;
}

// Save messages to firebase
function saveMessage(fname, fmail, fphone){
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
        fname:fname,
        fmail:fmail,
        fphone:fphone
    });
}