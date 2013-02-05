// JavaScript Document
function $(obj){
return document.getElementById(obj);
}
function change(n){
for (var i=1;i<4;i++){
if(n==i){
$("a"+i).style.zIndex="100";
}else{
$("a"+i).style.zIndex="0";
}
}
}