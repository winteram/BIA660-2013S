//create functions to make text follow mouse pointer.
function setup() {
                var el = getElementsByClassName('testClass');
               
                for(var i = 0; i < el.length; i++) {
                
                    var box = document.getElementById(el[i].id + '_box');
                        box.style.display = 'none';

                    el[i].onmouseover = function(e) {
                        var mousePos = getMouseLocation(e);

                        var box = document.getElementById(this.id + '_box');
                        box.style.display = 'block';
                        box.style.top = (mousePos[1]) + 'px';
                        box.style.left = (mousePos[0]+20) + 'px';
                    };
                    el[i].onmousemove = function(e) {                        
                        var mousePos = getMouseLocation(e);

                        var box = document.getElementById(this.id + '_box');
                        box.style.top = (mousePos[1]) + 'px';
                        box.style.left = (mousePos[0]+20) + 'px';
                    };
                    el[i].onmouseout = function() {
                        var box = document.getElementById(this.id + '_box');
                        box.style.display = 'none';
                    };
                }
            }

            function getMouseLocation(e) {
                if (!e) var e = window.event;
                if (e.pageX || e.pageY) {
                    posx = e.pageX;
                    posy = e.pageY;
                }
                else if (e.clientX || e.clientY) {
                    posx = e.clientX + document.body.scrollLeft    + document.documentElement.scrollLeft;
                    posy = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
                }
                return new Array(posx, posy);
            }
            window.onload = setup;
            
            function getElementsByClassName(className, tag, elm){
                var testClass = new RegExp("(^|\\s)" + className + "(\\s|$)");
                var tag = tag || "*";
                var elm = elm || document;
                var elements = (tag == "*" && elm.all)? elm.all : elm.getElementsByTagName(tag);
                var returnElements = [];
                var current;
                var length = elements.length;
                for(var i=0; i<length; i++){
                    current = elements[i];
                    if(testClass.test(current.className)){
                        returnElements.push(current);
                    }
                }
                return returnElements;
            }

//create the x scale and points with celebrities' names.
var xScale = d3.scale.ordinal() 
    .domain(["Justin Bieber", "Lady Gaga", "Taylor Swift", "Kim kardashian"])
    .rangePoints([240, 780]);
    
var xAxis = d3.svg.axis()
                  .scale(xScale)
                  .orient("bottom");


                      
var color = d3.scale.category10();  

//create a svg container.                
var svgContainer = d3.select("#JieRen").append("svg")
                                    .attr("width", 960)
                                   .attr("height", 400)
                                   ;
svgContainer.append("g")
    .call(xAxis);

//create functions to group data.
                                       
var stack = d3.layout.stack()
    .values(function(d) { return d.values; })
    .x(function(d) { return d.celebrity; })
    .y(function(d) { return d.value; })
    ;
    
var nest = d3.nest()
    .key(function(d) { return d.group; });
    
//insert data.    
var data = [
{ "group":"1", "celebrity":"1", "value": "7.6", "rx": 150, "ry": 200, "width": 160},
{ "group":"1", "celebrity":"2", "value": "10.2", "rx": 330, "ry": 200, "width": 160},
{ "group":"1", "celebrity":"3", "value": "11.7", "rx": 510, "ry": 200,"width": 160},
{ "group":"1", "celebrity":"4", "value": "2.14", "rx": 690, "ry": 200, "width": 160},
{ "group":"2", "celebrity":"1", "value": "29", "rx": 150, "ry": 300, "width": 160},
{ "group":"2", "celebrity":"2", "value": "28.8", "rx": 330, "ry": 300, "width": 160},
{ "group":"2", "celebrity":"3", "value": "18.6", "rx": 510, "ry": 300,"width": 160},
{ "group":"2", "celebrity":"4", "value": "12.3", "rx": 690, "ry": 300, "width": 160}
];

var dataByGroup = nest.entries(data);

stack(dataByGroup);

var group = svgContainer.selectAll(".group")
      .data(dataByGroup)
      .enter().append("g")
      .attr("class", "group");
      


 group.selectAll("rect")
      .data(function(d) { return d.values; })
      .enter().append("rect")
      .style("fill", function(d) { return color(d.group); });

//append text and set text attributes.
group.append("text")
      .attr("x", 30)
      .attr("y", 0)
      .transition()
      .duration(1000)
      .attr("y", function(d){return d.key*100+150;})
      .text(function(d){if (d.key==1){return "Sentiment Score";}
                        else if (d.key==2){return "Popularity";}
      })
      .style("font-size", "18px")
      .style("fill", function(d) { return color(d.key); })
      .attr("id", function(d) { return "text_"+d.key; })
      ;


//append rectangles and set attributes.      
group.selectAll("rect").attr("x", function(d) { return d.rx; })
                       .attr("y", 0)
                       .attr("width", function(d){return d.width;})
                       .attr("id", function(d){return "rect_"+d.group;})
                       .transition()
                       .duration(1000)
                       .attr("y", function(d){
                       var return_y;
                       if (Number(d.value)*5+30<30){
                       return_y= d.ry;
                       }
                       else if (Number(d.value)*5+30>=30){
                       return_y = Number(d.ry)-Math.abs(d.value)*2+100;
                       }
                       return return_y;})
                       .attr("height", function(d)
                       {return Math.abs(d.value)*2;})
                       .transition()
                       .delay(2000)
                       .duration(3000)
                       .attr("width", function(d){return d.width/3;})
                       .attr("x", function(d) { return d.group*57+d.rx-15; })
                       .attr("y", function(d){ return 300-Math.abs(d.value)*5+40;})
                       .attr("height", function(d)
                       {return Math.abs(d.value)*5+30;})
                       ;
                       
//create mouseover effects for the rects.

d3.selectAll("#rect_1").on("mouseover", function(){d3.selectAll("#rect_1").style("stroke","#1f77b4")&&d3.selectAll("#text_1").style("stroke","#1f77b4")}) 
                       .on("mouseout", function(){d3.selectAll("rect").style("stroke",null)&&d3.selectAll("#text_1").style("stroke",null)
                       });
                       
d3.selectAll("#rect_2").on("mouseover", function(){d3.selectAll("#rect_2").style("stroke","#ff7f0e")&&d3.selectAll("#text_2").style("stroke","#ff7f0e")}) 
                       .on("mouseout", function(){d3.selectAll("rect").style("stroke",null)&&d3.selectAll("#text_2").style("stroke",null)
                       });
