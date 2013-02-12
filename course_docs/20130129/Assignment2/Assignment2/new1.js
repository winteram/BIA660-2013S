var myVar=setInterval(function(){myTimer()},1000);
function myTimer()
{
var d=new Date();
var t=d.toLocaleTimeString();
document.getElementById("timer").innerHTML=t;
}
           var x=prompt("What is your name? ");
           var now = new Date();
    if(now.getHours() < 12)
        z="Good Morning";
     else
        z="Good Afternoon";  
     alert(z +" to our visitors, " + x +",  from "+geoplugin_city()+", "+geoplugin_countryName());
 
