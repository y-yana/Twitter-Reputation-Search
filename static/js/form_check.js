document.getElementById("submit-button").disabled = true;
const input = document.querySelector("text-field");

window.addEventListener('DOMContentLoaded',function(){
  document.getElementById('submit-button').disabled = true;
  document.getElementById('text-field').addEventListener('keyup',function(){
  if (this.value.length < 1) {
  document.getElementById('submit-button').disabled = true;
  } else {
  document.getElementById('submit-button').disabled = false;
  }
  },false);
  document.getElementById('text-field').addEventListener('change',function(){
  if (this.value.length < 1) {
  document.getElementById('submit-button').disabled = true;
  }
  },false);
  },false);