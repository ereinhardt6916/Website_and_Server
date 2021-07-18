
var elForm = document.getElementById('access');
var UsernameFeedback = document.getElementById('usernameFeedback'); 
var PasswordFeedback = document.getElementById('passwordFeedback'); 
var username = document.getElementById('username'); 
var password = document.getElementById('password');

//termsInput = document.getElementById('terms'); 
function hasLowerCase(str) {
    return str.toUpperCase() != str;
}

function hasUpperCase(str) {
    return str.toLowerCase() != str;
}

function hasNumber(myString) {
	return /\d/.test(myString);
  }

function checkUserName(event) {
	if (username.value.length < 7) {
		UsernameFeedback.innerHTML = '<----Username must be at least 7 chars';
		event.preventDefault();					// Do not submit the form (submit == default)
	} else {
		UsernameFeedback.innerHTML = '';		// Clear any error messages
	}
}
function checkPassword(event) {

	if (password.value.length < 7) {
		PasswordFeedback.innerHTML = '<----Password must be at least 7 chars';
		event.preventDefault();					// Do not submit the form (submit == default)
	}else if(hasNumber(password.value) == false){
		PasswordFeedback.innerHTML = '<----Password must have a number';
		event.preventDefault();	
	}else if(hasLowerCase(password.value) == false || hasUpperCase(password.value) == false){
		PasswordFeedback.innerHTML = '<----Password must have both cases';
		event.preventDefault();	
	}else{
		PasswordFeedback.innerHTML = '';
	}
		
	
}

// Create event listeners 
username.addEventListener('blur', function(event) {checkUserName(event); }, false); 
password.addEventListener('blur', function(event) {checkPassword(event); }, false); 

elForm.addEventListener('submit', function(event) {checkUserName(event); checkPassword(event);}, false); 
