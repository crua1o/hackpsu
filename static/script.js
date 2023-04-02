function validatePassword() {
    let password = document.getElementById("form3Example4c").value;
    let repeatPassword = document.getElementById("form3Example4cd").value;
    if (password != repeatPassword) {
      alert("Passwords do not match");
      return false;
    }
    return true;
}

  let selectedValue = document.querySelector('input[name="inlineRadioOptions"]:checked').value;

  // Set the value of the hidden input
  document.getElementById("genderInput").value = selectedValue;

function redirectToLogin() {
  //window.location.href = "{{ url_for('login') }}";
    window.location.href = "/login";
  console.log(window.location.href);

}

document.getElementById("login_redirect").addEventListener("click", redirectToLogin);


let samplechat = document.getElementById("samplechat");
let chatbox = document.getElementById("chatbox");
let map = document.getElementById("map");
let isLennyClicked = false;

function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];

    }
  }
}

function openChat() {
    if (!isLennyClicked) {
        isLennyClicked = true;
        map.style.filter = 'brightness(70%)';
        chatbox.style.opacity = 1;
    }
    else {
        isLennyClicked = false;
        map.style.filter = 'brightness(100%)';
        chatbox.style.opacity = 0;
    }

    closeQuestion();
}

function openQuestion() {
    if (isLennyClicked == false)
    samplechat.style.opacity = 1;
}

function closeQuestion() {
    samplechat.style.opacity = 0;
}

function getOptions() {
  let selectedOptions = document.querySelectorAll('input[type=checkbox]:checked');
  let values = [];
  for(let i = 0; i < selectedOptions.length; i++){
    values.push(selectedOptions[i].value);
  }
  console.log(values); // for testing purposes
  // Use AJAX to send the array to a Flask route
  // You can send it as a JSON object using the fetch API
  fetch('/homepage', {
    method: 'POST',
    body: JSON.stringify(values),
    headers: {
      'Content-Type': 'application/json'
    }
  });
}