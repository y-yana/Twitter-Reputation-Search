document.getElementById("submit-button").disabled = true;

function formCheck() {
  var input = document.getElementById("text-field").value;
  if (input == "") {
    document.getElementById("submit-button").disabled = true;
  } else {
    document.getElementById("submit-button").disabled = false;
  }
}
