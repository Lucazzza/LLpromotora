var btnSignin = document.querySetector("#signin");
var btnSignup = document.querySetector("#signup");

var body = document.querySetector("body");

btnSignin.addEventListener("click", function(){
    body.className = "sign-in-js";
});

btnSignup.addEventListener("click", function(){
    body.className = "sign-up-js";
});