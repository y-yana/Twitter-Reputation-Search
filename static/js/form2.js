var i = 2;

document.getElementById('text-field2').style.display = 'none';
document.getElementById('text-field3').style.display = 'none';
document.getElementById('text-field4').style.display = 'none';
document.getElementById('text-field5').style.display = 'none';

function addInput() {
  document.getElementById('text-field'+i).style.display = 'block';
  i++;
  if (i == 6) {
    document.getElementById("addbtn").disabled = true;
  }
}

document.getElementById('text-field1').onblur = function () {
  var input2 = document.getElementById("text-field1").value;
  if (input2 == "") {
    document.getElementById("submit-button").disabled = true;
  } else {
    document.getElementById("submit-button").disabled = false;
  }
}
