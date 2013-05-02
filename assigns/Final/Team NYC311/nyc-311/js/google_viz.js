   google.load("visualization", "1", {packages:["corechart"]});
   google.load('visualization', '1', {packages:['table']});
       
   google.load("visualization", "1", {packages:["corechart"]});
      function drawLine(data2) {
        var data = google.visualization.arrayToDataTable(data2);

        var options = {
          title: 'Complaints Trend'
        };

        var chart = new google.visualization.LineChart(document.getElementById('line_div'));
        chart.draw(data, options);
      }

      function drawChart(data2, area, div) {
        var data = google.visualization.arrayToDataTable(data2);

        var options = {
          title: area,
          vAxis: {title: 'Complaints',  titleTextStyle: {color: 'black'}}
        };

        var chart = new google.visualization.BarChart(document.getElementById(div));
        chart.draw(data, options);
      }

  
      
      function drawTable(data2, div) {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'ZipCode');
        data.addColumn('number', 'Avg Income');
        data.addColumn('number', 'Below Poverty Line');
        data.addColumn('number','Population');
        data.addRows(data2);
        var formatter = new google.visualization.NumberFormat({prefix: '$'});
        formatter.format(data, 1);
        var formatter2 = new google.visualization.NumberFormat({suffix: '%'});
        formatter2.format(data,2);
        var table = new google.visualization.Table(document.getElementById(div));
        table.draw(data, {showRowNumber: true});
      }

$(document).ready(function(){
  $("#chart_div1").hide();
  $("#table_div1").hide();
  $("#chart_div2").hide();
  $("#table_div2").hide();
  $("#line_div").hide();
  $("#tableau_div1").hide();
  $("#tableau_div2").hide();
    $("#test-button").click(function(){
            var selected1=$("#bar1 option:selected").text();
            var selected2=$("#bar2 option:selected").text();
            var selecteddate=$("#date_selection").val();
       
            $.post('/loadBarchart',{'selectedname1':selected1,'selectedname2':selected2,'viz_name':"linechart"},function(data){

              

              $("#line_div").fadeIn();
              drawLine(data);
             
             
            },'json')
            $.post('/loadBarchart',{'selectedname':selected1,'selecteddate':selecteddate,'viz_name':"barchart"},function(data){

              

              $("#chart_div1").fadeIn();
              drawChart(data,selected1,'chart_div1');
             
             
            },'json')

            $.post('/loadBarchart',{'selectedname':selected2,'selecteddate':selecteddate, 'viz_name':"barchart"},function(data){

              $("#chart_div2").fadeIn();
              drawChart(data,selected2,'chart_div2');
             
            },'json')
            $.post('/loadTable',{'selectedname':selected1},function(data){
              console.log("table load");
              $("#table_div1").fadeIn();
              drawTable(data,"table_div1");
            },'json')
            $.post('/loadTable',{'selectedname':selected2},function(data){
              console.log("table load");
              $("#table_div2").fadeIn();
              $("#tableau_div2").fadeIn();
              $("#tableau_div1").fadeIn();
              drawTable(data,"table_div2");
            },'json')
            console.log("Clicked");
        });
  });