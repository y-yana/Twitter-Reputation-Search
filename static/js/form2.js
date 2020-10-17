const btn = document.querySelector(".addbtn");
var count = 3;

btn.onclick =   function addform(){
  if(count <= 5){
    var newElement = document.createElement("input"); // input要素作成
    newElement.setAttribute("id","text-field"); // idを設定
    newElement.setAttribute("name","name"+count); // nameを設定
    newElement.setAttribute("placeholder","search word"); // placeholderを設定

    var parentDiv = document.getElementById("multiform");
    var childP1 = document.getElementsByName(".name2");
    parentDiv.insertBefore(newElement, childP1.nextSibling);
    count += 1;
  }
}
