// JavaScript Document
var activeTab =1;
var activeTabContent = 1;
var i;
for (i=2;i<=4;i++) {
 document.getElementById("tabContent"+i).style.display="none";
}
function showTabContent(n) {
 document.getElementById("tabContent"+activeTabContent).style.display="none";
 document.getElementById("tabContent"+n).style.display="";
 activeTabContent=n;
}
function showTab(n) {
 document.getElementById("tab"+activeTab).className="TabBarNormal";
 document.getElementById("tab"+n).className="TabBarActive";
 activeTab=n;
 showTabContent(n);
}