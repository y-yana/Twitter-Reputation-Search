function checkForm(){

  if(document.form.input.value == ""){
    alert("必須項目を入力して下さい。");
    return false;
  }else{
	  return true;
  }
}
