$('#hide_button').click(function(){
	$('#show').hide('slow');
});
$('#submit_button').click(function() {
	$('#show').show('slow');
	var my_index = document.getElementById("org_name").selectedIndex;
	var tag = document.getElementsByTagName("option")[my_index].value;
	console.log(tag);
	var url = "http://localhost:8080/" + tag;
	$.getJSON(url, function(my_json) {
		console.log(my_json[1].data);
		
		$(function () {
		    $('#show').highcharts({
		        chart: {
		            type: 'line',
		            marginRight: 130,
		            marginBottom: 25
		        },
		        title: {
		            text: 'NGDP_RPCH',
		            x: -20 //center
		        },
		        subtitle: {
		            text: 'Name Gross Domestic Product_Percent Change',
		            x: -20
		        },
		        xAxis: {
		            categories: ['2012','2013','2014','2015','2016','2017', '2018']
		        },
		        yAxis: {
		            title: {
		                text: 'Forecast(Percent)'
		            },
		            plotLines: [{
		                value: 0,
		                width: 1,
		                color: '#808080'
		            }]
		        },
		        tooltip: {
		            valueSuffix: '%'
		        },
		        legend: {
		            layout: 'vertical',
		            align: 'right',
		            verticalAlign: 'top',
		            x: -10,
		            y: 100,
		            borderWidth: 0
		        },
		        series: [{
		            name: my_json[0].country,
		            data: my_json[0].data
		        }, {
		            name: my_json[1].country,
		            data: my_json[1].data,
		        }, {
		            name: my_json[2].country,
		            data: my_json[2].data,
		        }, {
		            name: my_json[3].country,
		            data: my_json[3].data,
		        }]
		    });
		});
	});
});
