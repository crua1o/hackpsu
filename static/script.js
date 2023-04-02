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



