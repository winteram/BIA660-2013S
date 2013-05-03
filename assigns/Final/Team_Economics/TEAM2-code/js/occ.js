$('#occ_submit_button').click(function() {
	$('#occ_show').show('slow');
	var my_index = document.getElementById("occ_kind").selectedIndex;
	var tag = document.getElementsByTagName("option")[my_index+12].value;
	var url = "http://localhost:8080/" + tag;
	// console.log(tag);
	$.getJSON(url, function(my_json){
		var salary = new Array();
		var job_title = new Array();
		// console.log(my_json.length);
		for(var i=0;i<my_json.length;i++){
			salary[i]=parseInt(my_json[i].a_mean);

			job_title[i]=my_json[i].occ_title;
			// console.log(job_title[i]);
		}

		$(function () {
        $('#occ_show').highcharts({
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Annual average wages'
            },
            subtitle: {
                text: 'U.S. Department of Labor, Bureau of Economic analysis'
            },
            xAxis: {
                categories: job_title,
                title: {
                    text: null
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Salary mean (thousand)',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                }
            },
            tooltip: {
                valueSuffix: ' thousand'
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
		            name: "salary",
		            data: salary
		        }]
        });
    });

	});
});