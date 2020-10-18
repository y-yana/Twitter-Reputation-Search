var i = 2;

function addInput() {
  var input_data = document.createElement('input');
  input_data.type = 'text';
  input_data.name = 'name' + i;
  input_data.placeholder = 'search word';
  var parent = document.getElementById('form_area');
  parent.appendChild(input_data);
  i++;
  if (i == 6) {
    document.getElementById("addbtn").disabled = true;
  }
}
