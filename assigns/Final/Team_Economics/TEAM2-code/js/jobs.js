$('#jobs_hide_button').click(function(){
	$('#jobs_show').hide('slow');
});
$('#jobs_submit_button').click(function() {
	$('#jobs_show').show('slow');
	var my_index = document.getElementById("kind").selectedIndex;
	var jobs_tag = document.getElementsByTagName("option")[my_index+3].value;
	var my_year = document.getElementById("years").selectedIndex;
	var year = document.getElementsByTagName("option")[my_year+9].value;

	var url = "http://localhost:8080/jobs?code=" + jobs_tag + "&year=" + year;
	console.log(url)
	$.getJSON(url, function(json) {
		console.log(json[0].value);

		$(function () {
	        $('#jobs_show').highcharts({
	            chart: {
	                type: 'bar'
	            },
	            title: {
	                text: 'Job opens and hires'
	            },
	            subtitle: {
	                text: 'US Job information'
	            },
	            xAxis: {
	                categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
	                title: {
	                    text: null
	                }
	            },
	            yAxis: {
	                min: 0,
	                title: {
	                    text: 'Number (Thousand )',
	                    align: 'high'
	                },
	                labels: {
	                    overflow: 'justify'
	                }
	            },
	            tooltip: {
	                valueSuffix: ' Thousand'
	            },
	            plotOptions: {
	                bar: {
	                    dataLabels: {
	                        enabled: true
	                    }
	                }
	            },
	            legend: {
	                layout: 'vertical',
	                align: 'right',
	                verticalAlign: 'top',
	                x: -100,
	                y: 100,
	                floating: true,
	                borderWidth: 1,
	                backgroundColor: '#FFFFFF',
	                shadow: true
	            },
	            credits: {
	                enabled: false
	            },
	            series: [{
	                name: 'Jobs open',
	                data: json[0].value
	            }, {
	                name: 'Jobs hire',
	                data: json[1].value
	            }]
	        });
	    });		
	});
});
